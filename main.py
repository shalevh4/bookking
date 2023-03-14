from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from flaskext.mysql import MySQL
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session
from People import People
from Customer import Customer
from Librarian import Librarian
from Book import Book
from Books_in_branch import Books_in_branch
from Branch import Branch
from Copy import Copy
from Borrow import Borrow
from Order import Order


# This is the view function for the welcome page of the site
@app.route("/")
def index():
    if "email" in session and session["email"] != None:
        cursor.execute("SELECT email_address FROM librarian WHERE email_address=%s", session['email'])
        if cursor.fetchall() != ():
            curr_lib = Librarian()
            curr_lib.email = session['email']
            full_name = curr_lib.find_full_name()
            return render_template("homepage_librarian.html", email=curr_lib.email, full_name=full_name)
        else:
            curr_cust = Customer()
            curr_cust.email = session['email']
            full_name = curr_cust.find_full_name()
            return render_template("homepage_customer.html", email=curr_cust.email, full_name=full_name)
    else:
        return render_template('index.html')


# This is the view function for the registration page of a new customer
@app.route("/register_customer", methods=["POST", "GET"])
def register_customer():
    if request.method == "POST":
        # declaring different variables
        curr_customer = Customer()
        curr_customer.email = request.form["email"]
        curr_customer.password = request.form["password"]
        curr_customer.first_name = request.form["first_Name"]
        curr_customer.last_name = request.form["last_Name"]
        curr_customer.phone_number = request.form["phone"]
        curr_customer.date_of_birth = request.form["date_of_birth"]
        curr_customer.city = request.form["city"]
        curr_customer.street = request.form["street"]
        curr_customer.house_number = request.form["house_num"]
        # Error handling
        if curr_customer.check_if_in_db():
            flash("Email already exist.")
            return redirect("/register_customer")
        elif datetime.strptime(curr_customer.date_of_birth, "%Y-%m-%d") > datetime.now():
            flash("Wrong date of birth")
            return redirect("/register_customer")
        # Insertion of new customer to the DB
        else:
            curr_customer.insert_to_db()
            # Saving the customer email for future entrances to the site
            session['email'] = curr_customer.email
            # Redirect the registered customer to it's homepage
            return redirect("/homepage_customer")
    return render_template("register_customer.html", all_data=cursor.fetchall())


# This is the view function for the registration page of a new customer
@app.route("/register_librarian", methods=["POST", "GET"])
def register_librarian():
    if request.method == "POST":
        # declaring different variables
        curr_librarian = Librarian()
        curr_librarian.email = request.form["email"]
        curr_librarian.password = request.form["password"]
        curr_librarian.first_name = request.form["first_Name"]
        curr_librarian.last_name = request.form["last_Name"]
        curr_librarian.phone_number = request.form["phone"]
        curr_librarian.branch_number = request.form["branch_name"]
        curr_librarian.branch_number = curr_librarian.find_branch_number_by_name()
        curr_librarian.city = request.form["city"]
        curr_librarian.street = request.form["street"]
        curr_librarian.house_number = request.form["house_num"]
        temp = Branch()
        temp.branch_number = curr_librarian.branch_number
        # Error handling
        if curr_librarian.check_if_in_db():
            flash("Email already exist")
            return redirect("/register_librarian")
        elif not temp.check_if_in_db():
            flash("branch number don't exist")
            return redirect("/register_librarian")
        # Insertion of new librarian to the DB
        else:
            curr_librarian.insert_to_db()
            # Saving the librarian email for future entrances to the site
            session['email'] = curr_librarian.email
            # Redirect the registered librarian to it's homepage
            return redirect("/homepage_librarian")
    cursor.execute("SELECT branch_name FROM branch")
    return render_template("register_librarian.html", all_data=cursor.fetchall())


# This is the view function of the librarian homepage
@app.route("/homepage_librarian")
def homepage_librarian():
    curr_lib = Librarian()
    curr_lib.email = session['email']
    # Finds the librarian full name to show him a welcome message in his homepage
    full_name = curr_lib.find_full_name()
    return render_template("homepage_librarian.html", email=curr_lib.email, full_name=full_name)


# This is the view function of the librarian login page
@app.route("/login_librarian", methods=["POST", "GET"])
def login_librarian():
    if request.method == "POST":
        curr_librarian = Librarian()
        curr_librarian.email = request.form["email"]
        curr_librarian.password = request.form["password"]
        logged_email = curr_librarian.login()
        # Check if the librarian exist in our DB
        if logged_email == ():
            flash("Wrong email or password")
            return redirect("/login_librarian")
        else:
            # Saving librarian's email for future entrances
            session['email'] = logged_email
        connection.commit()
        # Redirect the librarian to its homepage if the login was successful
        return redirect("/homepage_librarian")
    return render_template("login_librarian.html")


# This is the view function of the customer homepage
@app.route("/homepage_customer")
def homepage_customer():
    curr_cust = Customer()
    curr_cust.email = session['email']
    # Finds the customer full name to show him a welcome message in his homepage
    full_name = curr_cust.find_full_name()
    return render_template("homepage_customer.html", email=curr_cust.email, full_name=full_name)


# This is the view function of the customer login page
@app.route("/login_customer", methods=["POST", "GET"])
def login_customer():
    if request.method == "POST":
        curr_cust = Customer()
        curr_cust.email = request.form["email"]
        curr_cust.password = request.form["password"]
        logged_email = curr_cust.login()
        # Check if the customer exist in our DB
        if logged_email == ():
            flash("Wrong email or password")
            return redirect("/login_customer")
        else:
            # Saving customer's email for future entrances
            session['email'] = logged_email
        connection.commit()
        # Redirect the customer to its homepage if the login was successful
        return redirect("/homepage_customer")
    return render_template("login_customer.html")


# This method is the view function for the insertion of new book by a librarian
@app.route("/add_copy", methods=["POST", "GET"])
def add_copy():
    if request.method == "POST":
        curr_book = Book()
        curr_book.book_number = request.form["book_number"]
        curr_copy = Copy()
        # Check if there are already other copies of this book in the DB
        # If the book is already in the DB it adds a new copy of it
        if curr_book.check_if_in_db():
            curr_copy.book_name = curr_book.find_book_name_by_number()[0]
            curr_copy.book_number = curr_book.book_number
            curr_copy.insert_to_db()
            connection.commit()
            flash("A copy of this book was added to your branch.")
            return redirect('/add_copy')
        # If the book isn't in the DB it redirects the librarian to other page where he can enter it's details
        else:
            session["book_number"] = curr_book.book_number
            return redirect("/collect_book_info")
    return render_template('insert_book.html')


# This is the view function for the page where the librarian insert new book to the system
@app.route("/collect_book_info", methods=["POST", "GET"])
def collect_book_info():
    if request.method == "POST":
        # Getting the form details from the html
        curr_book = Book()
        curr_book.book_name = request.form["book_name"]
        curr_book.book_number = session["book_number"]
        curr_book.author_name = request.form["author_name"]
        curr_book.year_published = request.form["year_published"]
        curr_book.publisher = request.form["publisher"]
        # Insert the new book details to the DB
        curr_book.insert_to_db()
        curr_copy = Copy()
        curr_copy.book_number = curr_book.book_number
        curr_copy.insert_to_db()
        connection.commit()
        # Success message
        flash("A new book was added to the database and a copy was added to your branch.")
        return redirect('/collect_book_info')
    return render_template("collect_book_data.html")


# This is the view function for the page where the librarian can enter a new book borrow for a customer
@app.route('/check_availability', methods=['POST', 'GET'])
def check_availability():
    default_return = date.today() + timedelta(days=14)
    if request.method == 'POST':
        curr_cust = Customer()
        curr_copy = Copy()
        curr_copy.book_number = request.form['book_number']
        curr_cust.email = request.form['customer_email']
        return_date = request.form['return_date']
        curr_book_in_branch = Books_in_branch()
        curr_book_in_branch.book_number = curr_copy.book_number
        copy_numbers = curr_copy.find_copy_numbers_by_book()
        # finds the branch # by the session email
        curr_book_in_branch.branch_number = curr_book_in_branch.find_branch_by_email()
        # Query the database to check the availability of the book
        book_availability = curr_book_in_branch.book_availability()
        # check the email belongs to existing customer
        customer_check = curr_cust.check_if_in_db()
        # check the user don't have more than 3 active borrow
        num_of_borrow = curr_cust.count_borrow()
        # check if the user has ordered the book he wants to borrow
        curr_order = Order()
        curr_order.customer_email = curr_cust.email
        was_invited = curr_order.customer_invited(copy_numbers)
        # check for all cases the user can fill and call for the relevant page based on the info entered by the Librarian
        if num_of_borrow == True:
            flash("This customer has reached the maximum amount of active borrows.")
            return redirect('/check_availability')
        elif was_invited[0] == True:
            curr_borrow = Borrow()
            curr_borrow.borrow_date = str(date.today())
            curr_borrow.return_date = return_date
            curr_borrow.copy_number = was_invited[1]
            curr_borrow.customer_email = curr_cust.email
            curr_borrow.insert_to_db()
            connection.commit()
            curr_order.update_status_to_completed(was_invited[1])
            curr_copy.update_status_to_borrowed(was_invited[1])
            curr_book_in_branch.find_amount_available()
            flash("The order has been completed and the book was successfully borrowed, there are {0} more available copies in branch".format(curr_book_in_branch.amount_available))
            return redirect("/check_availability")
        elif book_availability == True and customer_check == True:
            curr_borrow = Borrow()
            curr_borrow.borrow_date = str(date.today())
            curr_borrow.return_date = return_date
            branch_num = curr_book_in_branch.branch_number
            curr_borrow.copy_number = curr_copy.attach_copy(curr_copy.book_number, branch_num)
            curr_borrow.customer_email = curr_cust.email
            curr_borrow.insert_to_db()
            connection.commit()
            curr_book_in_branch.find_amount_available()
            flash("The book was successfully borrowed,there are {0} more copies available in branch.".format(curr_book_in_branch.amount_available))
            return redirect("/check_availability")
        elif book_availability == False and customer_check == False:
            flash("Both book number and email address are wrong.")
            return redirect("/check_availability")
        elif book_availability == False:
            flash("This book isn't available.")
            return redirect("/check_availability")
        elif not curr_cust.check_if_in_db():
            flash("There is no customer using this email address.")
            return redirect("/check_availability")
    else:
        default_return = date.today() + timedelta(days=14)
        return render_template('book_availability.html', default_return=default_return)


# This is the view function for the page where a customer can search for a book by name/author
@app.route('/search_for_book', methods=['POST', 'GET'])
def search_for_book():
    if request.method == 'POST':
        # Error handling for cases where the user hasn't entered any detail or entered both book name and book author
        if request.form['author_name'] == "" and request.form['book_name'] == "":
            flash("Please type a book name or author name.")
            return redirect('/search_for_book')
        if request.form['author_name'] != "" and request.form['book_name'] != "":
            flash("Please search by only one parameter.")
            return redirect('/search_for_book')
        # Show results for search by book name
        else:
            curr_book = Book()
            if request.form['author_name'] == "":
                curr_book.book_name = request.form['book_name']
                curr_book.book_number = curr_book.find_book_number()
                if curr_book.book_number == ():
                    flash("There isn't a book in the system with this name")
                    return redirect('/search_for_book')
                all_data = curr_book.check_availability_in_branch()
                return render_template('book_search_result.html', all_data=all_data)
            # Show results for search by author name
            elif request.form['book_name'] == "":
                curr_book.author_name = request.form['author_name']
                curr_book.book_number = curr_book.find_book_number_by_author()
                if curr_book.book_number == ():
                    flash("There isn't a book in the system written by this author")
                    return redirect('/search_for_book')
                all_data = curr_book.check_availability_in_branch()
                return render_template('book_search_result.html', all_data=all_data)
    return render_template('book_search.html')


# This is the view function for the page where the customer can see its borrow history and extend active borrow
@app.route("/borrow_history", methods=["POST", "GET"])
def borrow_history():
    curr_cust = Customer()
    curr_cust.email = session["email"]
    all_data = curr_cust.find_borrow_history()
    return render_template("borrow_history.html", all_data=all_data)


# This is the view function for the page where the librarian insert new book to the system
@app.route("/order_book", methods=["POST", "GET"])
def order_book():
    if request.method == "POST":
        order = Order()
        # Error handling for cases where the book isn't available at all or in the specific branch the user searched for
        if order.check_exist_branches():
            flash("Were sorry, we don't have this book in any of our branches.")
            return redirect("/order_book")
        elif order.check_exist_branch():
            flash("Were sorry, we don't have this book in this branch.")
            return redirect("/order_book")
        elif True:
            temp_data = order.same_name()
            # Check if the book name entered by a customer is appearing more than once in our DB
            # If so, the user is redirected to a page where he can choose what book to order
            if temp_data[0] == True:
                all_data = temp_data[1]
                return render_template('order_book_same_name.html', all_data=all_data)
        book_num = temp_data[1]
        branch_num = temp_data[2]
        copies_to_order = order.find_copy_to_order(book_num, branch_num)
        # Error handling for cases where the desired book is available to borrow or isn't available to order due to high demand
        if copies_to_order == 'Available to borrow':
            flash("No need to order, there is a copy available at the branch.")
            return redirect("/order_book")
        elif copies_to_order is True:
            flash("Were sorry, the book isn't available due to high demand.")
            return redirect("/order_book")
        # In case there are no errors we allow the order and enter it's details to the DB
        else:
            over_borrowing = False
            # check if the user currently has 3 active borrows
            cursor.execute("SELECT count(borrow.copy_number) FROM borrow JOIN copy ON copy.copy_number = borrow.copy_number WHERE customer_email =%s AND return_date >= %s and copy.current_status = 'borrowed'", (session["email"], date.today()))
            if int(cursor.fetchone()[0]) >= 3:
                over_borrowing = True
            order.order_date = date.today()
            order.order_status = 'currently borrowed'
            order.copy_number = copies_to_order
            order.customer_email = session["email"]
            order.insert_to_db()  # An order is received in the system
            connection.commit()
            if over_borrowing:
                flash("The order was successfully placed. Please note that you are currently lending 3 books, it is not possible to borrow more than this number of books. When borrowing a new book, one of the books must be returned.")
            else:
                flash("The order was successfully placed.")
            return redirect("/order_book")
    cursor.execute("SELECT branch_name FROM branch")
    return render_template("order_book.html", all_data=cursor.fetchall())


# This is the view function for the page where the customer can choose what book he wants to order
@app.route("/order_book_same_name", methods=["POST", "GET"])
def order_book_same_name():
    if request.method == "POST":
        order = Order()
        book_num = request.form['subject']
        branch_num = session['branch']
        copies_to_order = order.find_copy_to_order(book_num, branch_num)
        # Error handling same to order book function
        if copies_to_order == 'Available to borrow':
            flash("No need to order, there is a an available copy at the branch.")
            return redirect("/order_book_same_name")
        elif copies_to_order is True:
            flash("Were sorry, the book isn't available due to high demand.")
        else:
            over_borrowing = False
            cursor.execute("SELECT count(borrow.copy_number) FROM borrow JOIN copy ON copy.copy_number = borrow.copy_number WHERE customer_email =%s AND return_date >= %s and copy.current_status = 'borrowed'", (session["email"], date.today()))
            if int(cursor.fetchone()[0]) >= 3:
                over_borrowing = True
            order.order_date = date.today()
            order.order_status = 'currently borrowed'
            order.copy_number = copies_to_order
            order.customer_email = session["email"]
            order.insert_to_db()  # An order is received in the system
            connection.commit()
            if over_borrowing:
                flash("The order was successfully placed.\n Please note that you are currently lending 3 books, it is not possible to borrow more than this number of books.\n When borrowing a new book, one of the books must be returned.")
            else:
                flash("The order was successfully placed.")
            return redirect("/order_book_same_name")
    return render_template("order_book_same_name.html")


# This is the view function for the page where the customer can see all of his orders
@app.route("/customer_orders", methods=["POST", "GET"])
def customer_orders():
    curr_cust = Customer()
    curr_cust.email = session["email"]
    results = curr_cust.find_customer_orders()
    return render_template('customer_orders.html', results=results)


# This is the view function for the action where the customer can extend his borrow by another week
@app.route("/extend_borrow", methods=["POST", "GET"])
def extend_borrow():
    if request.method == "POST":
        curr_borrow = Borrow()
        curr_borrow.copy_number = request.form["extend_borrow"]
        curr_borrow.customer_email = session["email"]
        curr_order = Order()
        curr_order.copy_number = curr_borrow.copy_number
        # Check if the desired book has been ordered by other customer
        # If the book wasn't ordered the borrow will be extend by another week
        if curr_order.is_invited():
            curr_borrow.extend_borrow()
            connection.commit()
            flash("The borrow was extended in another week.")
            return redirect('/borrow_history')
        # If the book was ordered the extension won't be possible
        else:
            flash("Sorry, this book is already ordered.")
            return redirect('/borrow_history')
    else:
        return render_template("borrow_history.html")


# This is the view function for logout from the system
@app.route("/logout")
def logout():
    # Deletes the email saved in the session
    session["email"] = None
    return redirect("/")


# This function runs every time the site run and checks for borrows that their return date expired
def update_borrow_status():
    curr_borrow = Borrow()
    curr_order = Order()
    curr_copy = Copy()
    curr_book_in_branch = Books_in_branch()
    copies_list = curr_borrow.expired_borrow()
    for copy_number in copies_list:
        curr_order.copy_number = copy_number
        curr_copy.copy_num = copy_number
        # Check if the copy number attached to specific borrow expired wasn't ordered by other customer
        res = curr_order.is_invited()
        curr_copy.book_number = curr_copy.find_book_number_by_copy()
        curr_book_in_branch.book_number = curr_copy.find_book_number_by_copy()
        # If the copy wasn't ordered it will be back available
        if res == True:
            curr_copy.update_status_to_available()
            curr_book_in_branch.update_amount_available()
        # If the copy wasn't ordered it's status will change to ordered and the customer ordered it will be able to pick it from the library
        else:
            curr_copy.update_status_to_ordered()
            curr_order.update_status_to_in_library()
    connection.commit()


# This function runs every time the site run and checks which order is in the branch for more than 3 days and changes the relevant fields in DB
def update_order_status():
    curr_order = Order()
    curr_copy = Copy()
    curr_book_in_branch = Books_in_branch()
    copies_list = curr_order.expired_order()
    # For each copy that is waiting for more than 3 days it's status will be available and the order status will be changed to expired
    for copy_number in copies_list:
        curr_order.copy_number = copy_number
        curr_copy.copy_num = copy_number
        curr_order.update_status_to_expired()
        curr_copy.update_status_to_available()
        curr_book_in_branch.book_number = curr_copy.find_book_number_by_copy()
        curr_book_in_branch.update_amount_available()
    connection.commit()


# Call for the function that needs to update the DB
update_borrow_status()
update_order_status()

if __name__ == "__main__":
    app.run(debug=True)
    cursor.close()
    connection.close()

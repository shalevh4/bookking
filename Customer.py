# This class contains all the relevant methods for the customer activity
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session
from People import People


class Customer(People):
    # initiate the customer object
    def __init__(self):
        People.__init__(self)
        self.date_of_birth = ""

    # This method handles the login process of an existing customer to the site
    def login(self):
        cursor.execute("SELECT email_Address FROM customer WHERE email_address=%s and password=%s",
                       (self.email, self.password))
        return cursor.fetchall()

    # This method handles the insertion of a new customer to the DB
    def insert_to_db(self):
        cursor.execute(
            "INSERT INTO customer(email_address,password,first_name,last_name,phone_number,date_of_birth,city,street,house_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (self.email, self.password, self.first_name, self.last_name,
             self.phone_number, str(self.date_of_birth), self.city, self.street,
             self.house_number))
        connection.commit()

    # This method checks if a customer email is already exist in the DB
    def check_if_in_db(self):
        cursor.execute("SELECT email_address FROM customer WHERE email_address=%s",
                       self.email)
        return cursor.fetchall() != ()

    # This method finds a customer borrow history by it's email
    def find_borrow_history(self):
        # the relevant information about borrows of specific customer can be received from the combination between copy and borrow tables
        cursor.execute(
            "SELECT copy.copy_number, book_name, branch_name, borrow_date, return_date FROM borrow JOIN copy ON borrow.copy_number = copy.copy_number JOIN book on copy.book_number = book.book_number JOIN branch on branch.branch_number = copy.branch_number WHERE borrow.customer_email = %s AND borrow.return_date >= CURRENT_DATE", self.email)
        all_data_list = []
        # Creating list of tuples that will contain all the borrows a specific customer did sorted by their return date
        for row in cursor:
            temp_list = list(row)
            temp_list.append(True)
            temp_tuple = tuple(temp_list)
            all_data_list.append(temp_tuple)
        cursor.fetchall()
        all_data_list = sorted(all_data_list, key=lambda x: x[4], reverse=True)
        # Query meant to find all the borrows that a specific customer did but their return date already passed
        cursor.execute(
            "SELECT copy.copy_number, book_name, branch_name, borrow_date, return_date FROM borrow JOIN copy ON borrow.copy_number = copy.copy_number JOIN book on copy.book_number = book.book_number JOIN branch on branch.branch_number = copy.branch_number WHERE borrow.customer_email=%s AND borrow.return_date < CURRENT_DATE",
            self.email)
        expired_borrows = []
        for row in cursor:
            temp_list = list(row)
            temp_list.append(False)
            temp_tuple = tuple(temp_list)
            expired_borrows.append(temp_tuple)
        cursor.fetchall()
        expired_borrows = sorted(expired_borrows, key=lambda x: x[4], reverse=True)
        all_data_list = all_data_list + expired_borrows
        return tuple(all_data_list)

    # This method returns True is the customer has already 3 active book borrowings
    def count_borrow(self):
        cursor.execute("SELECT COUNT(*) FROM borrow JOIN copy ON borrow.copy_number = copy.copy_number WHERE customer_email = %s AND CURRENT_DATE < return_date and copy.current_status = 'borrowed'", self.email)
        count = cursor.fetchone()[0]
        return count >= 3

    # This method finds a customer orders by it's email
    def find_customer_orders(self):
        cursor.execute(
            "SELECT o.order_date, b.book_name, o.order_status, c.branch_number, bor.return_date FROM orders o JOIN copy c ON o.copy_number = c.copy_number JOIN book b ON c.book_number = b.book_number JOIN borrow bor ON o.copy_number = bor.copy_number WHERE o.customer_email=%s AND o.order_date BETWEEN bor.borrow_date AND bor.return_date",
            self.email)
        inital_results = cursor.fetchall()
        # Creating list of tuples where each contain all the relevant date regarding specific customer orders
        middle_results = []
        for row in inital_results:
            temp_row = list(row)
            if temp_row[2] == 'in library':
                last_date = temp_row[4] + timedelta(days=3)
                temp_row.append(last_date)
                middle_results.append(temp_row)
            else:
                middle_results.append(temp_row)
        final_results = tuple([tuple(x) for x in middle_results])
        return final_results

    # This method returns the full name of the customer by its email address
    def find_full_name(self):
        cursor.execute("SELECT first_name, last_name FROM customer WHERE email_address = %s", self.email)
        result = cursor.fetchall()
        full_name = result[0][0] + ' ' + result[0][1]
        return full_name

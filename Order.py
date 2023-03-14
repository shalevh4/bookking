# This class contains all the relevant methods for borrow related actions
from flask import Flask, render_template, redirect, request, session, flash
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session
from Book import Book
from Branch import Branch


class Order:
    # initiate the borrow object
    def __init__(self):
        self.order_date = ''
        self.order_status = ''
        self.copy_number = 0
        self.customer_email = ''

    # This method handles the insertion of a new ordering to the DB
    def insert_to_db(self):
        cursor.execute(
            "INSERT INTO orders(order_date,order_status,copy_number,customer_email) VALUES(%s,%s,%s,%s)",
            (self.order_date, self.order_status, self.copy_number, self.customer_email))
        connection.commit()

    def same_name(self):
        book = Book()
        branch = Branch()
        branch_name = request.form["branch_name"]
        cursor.execute("SELECT branch_number FROM branch where branch_name = %s", branch_name)
        branch.branch_number = cursor.fetchall()[0][0]
        session['branch'] = branch.branch_number
        book.book_name = request.form["book_name"]
        cursor.execute('select * from book where book_name = %s', book.book_name)
        books_list = list(cursor.fetchall())
        for book in books_list:
            cursor.execute("SELECT * FROM books_in_branch WHERE book_number = %s and branch_number = %s", (book[0], branch.branch_number))
            if cursor.fetchall() == ():
                books_list.remove(book)
        # Checks if there are two different books with the same name
        if len(books_list) > 1:
            return True, books_list, branch.branch_number
        else:
            return False, books_list[0][0], branch.branch_number

    def find_copy_to_order(self, book_num, branch_num):
        book = Book()
        branch = Branch()
        branch.branch_number = branch_num
        book.book_number = book_num
        cursor.execute("SELECT * FROM copy WHERE book_number = %s AND current_status = 'available' AND branch_number = %s", (book.book_number, branch.branch_number))
        if cursor.fetchall() != ():
            return 'Available to borrow'
        cursor.execute("select copy.copy_number, borrow.borrow_date, borrow.return_date FROM copy join borrow ON copy.copy_number = borrow.copy_number where borrow.return_date>= %s and copy.current_status = 'borrowed' and book_number = %s and copy.branch_number = %s ORDER BY borrow.return_date ASC", (date.today(), book.book_number, branch.branch_number))
        borrowed_copies = []
        for row in cursor:
            temp = list(row)
            borrowed_copies.append(temp)
        cursor.fetchall()
        for copy in borrowed_copies:
            cursor.execute("SELECT * FROM orders WHERE copy_number = %s AND order_date>=%s", (copy[0], copy[1]))
            if cursor.fetchall() == ():
                return copy[0]
        return True

    # Checks if the book is exist in the specific branch
    def check_exist_branch(self):
        book = Book()
        branch = Branch()
        branch_name = request.form["branch_name"]
        cursor.execute("SELECT branch_number FROM branch where branch_name = %s", branch_name)
        branch.branch_number = cursor.fetchall()[0]
        book.book_name = request.form["book_name"]
        book.book_number = book.find_book_number()
        cursor.execute("SELECT * FROM books_in_branch WHERE branch_number = %s AND book_number in %s ", (branch.branch_number, book.book_number))
        return cursor.fetchall() == ()

    # Checks if a book is exist in the library branches
    def check_exist_branches(self):
        book = Book()
        book.book_name = request.form["book_name"]
        cursor.execute("SELECT * FROM book WHERE book_name = %s ", book.book_name)
        return cursor.fetchall() == ()

    # This method checks if the copy related to specific borrow ended is also ordered by customer
    def is_invited(self):
        cursor.execute("SELECT copy_number FROM orders WHERE copy_number = %s AND order_status = 'currently borrowed'", self.copy_number)
        return cursor.fetchall() == ()

    # This method updates the status of active order to indicate the book is available in the library
    def update_status_to_in_library(self):
        cursor.execute("UPDATE orders SET order_status = 'in library' WHERE copy_number = %s AND order_status = 'currently borrowed'", self.copy_number)

    # This method updates the status of active order waited to the customer in library to be completed
    def update_status_to_completed(self, copy_number):
        cursor.execute("UPDATE orders SET order_status = 'completed' WHERE copy_number = %s AND order_status = 'in library'", copy_number)

    # This method updates the status of active order waited to the customer in library to be expired
    def update_status_to_expired(self):
        cursor.execute("UPDATE orders SET order_status = 'expired' WHERE copy_number = %s AND order_status = 'in library'", self.copy_number)

    # This method returns a list of copies number that are waiting for more than 3 days to be borrowed
    def expired_order(self):
        cursor.execute("SELECT o.copy_number FROM orders o JOIN borrow b ON o.copy_number = b.copy_number WHERE o.order_date BETWEEN b.borrow_date AND b.return_date AND o.order_status = 'in library' AND DATEDIFF(CURRENT_DATE, return_date)>3")
        results = cursor.fetchall()
        return [row[0] for row in results]

    # This method checks if the customer ordered the book he wants to borrow
    def customer_invited(self, copy_numbers):
        cursor.execute("SELECT copy_number FROM orders WHERE customer_email = %s and order_status = 'in library'", self.customer_email)
        results = cursor.fetchall()
        customer_active_orders = [row[0] for row in results]
        for copy_number in customer_active_orders:
            if copy_number in copy_numbers:
                return True, copy_number
            else:
                continue
        return False, None

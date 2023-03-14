# This class contains all the relevant methods for copy related actions
from datetime import datetime, date, timedelta
from flask import Flask, render_template, redirect, request, session, flash
from db_connection import app, connection, cursor, Session


class Copy:
    # initiate the copy object
    def __init__(self):
        self.copy_num = 0
        self.current_status = ""
        self.book_number = 0
        self.branch_number = 0

    # This method handles the insertion of a new copy of a specific book to the DB
    def insert_to_db(self):
        temp_email = session["email"]
        # This query meant to find the branch number of specific copy out of his email address
        cursor.execute(
            "SELECT branch_number FROM librarian WHERE email_address=%s", temp_email)
        self.branch_number = cursor.fetchall()[0]
        cursor.execute(
            "INSERT INTO copy(current_status,book_number,branch_number) VALUES(%s,%s,%s)",
            ("available", self.book_number, self.branch_number))
        cursor.execute("SELECT * FROM books_in_branch WHERE book_number=%s AND branch_number=%s",
                       (self.book_number, self.branch_number))
        # If this book exist in our db but not in the branch so it will add its first copy to the copy list and a record of the book in branch
        if cursor.fetchall() == ():
            cursor.execute(
                "INSERT INTO books_in_branch(amount_in_stock,amount_available,book_number,branch_number) VALUES(%s,%s,%s,%s)",
                (0, 0, self.book_number, self.branch_number))
        cursor.execute(
            "UPDATE books_in_branch SET amount_in_stock = amount_in_stock +1 ,amount_available = amount_available +1 WHERE ((book_number=%s) AND (branch_number=%s));",
            (self.book_number, self.branch_number))
        connection.commit()

    # This method is responsible to connect a specific borrowing to a specific copy of the book borrowed
    def attach_copy(self, book_num, branch_num):
        self.book_number = book_num
        cursor.execute('SELECT copy_number FROM copy WHERE book_number=%s AND current_status=%s AND branch_number =%s', (self.book_number, 'available', branch_num))
        res = cursor.fetchone()[0]
        cursor.execute("UPDATE copy SET current_status = 'borrowed' WHERE copy_number=%s", res)
        cursor.execute("UPDATE books_in_branch SET amount_available = amount_available -1 WHERE book_number=%s and branch_number = %s", (book_num, branch_num))
        connection.commit()
        return res

    # This method finds the book number out of the copy number
    def find_book_number_by_copy(self):
        cursor.execute("SELECT book_number FROM copy WHERE copy_number=%s",
                       self.copy_num)
        return cursor.fetchone()[0]

    # This method returns a list of copy numbers of specific book
    def find_copy_numbers_by_book(self):
        cursor.execute("SELECT copy_number FROM copy WHERE book_number = %s", self.book_number)
        results = cursor.fetchall()
        return [row[0] for row in results]

    # This method updates the copy status back to available
    def update_status_to_available(self):
        cursor.execute("UPDATE copy SET current_status = 'available' WHERE copy_number = %s", self.copy_num)

    # This method updates the copy status to borrowed when the customer takes the book he ordered
    def update_status_to_borrowed(self, copy_number):
        cursor.execute("UPDATE copy SET current_status = 'borrowed' WHERE copy_number = %s", copy_number)

    # This method updates the copy status back to ordered
    def update_status_to_ordered(self):
        cursor.execute("UPDATE copy SET current_status = 'ordered' WHERE copy_number = %s", self.copy_num)

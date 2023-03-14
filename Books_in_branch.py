# This class contains all the relevant methods related to the connection between a specific branch and a specific book
from datetime import datetime, date, timedelta
from flask import Flask, render_template, redirect, request, session, flash
from db_connection import app, connection, cursor, Session


class Books_in_branch:
    # initiate the books in branch object
    def __init__(self):
        self.branch_number = 0
        self.book_number = 0
        self.amount_in_stock = 0
        self.amount_available = 0

    # This method allows us to find how many copies of specific book are available in a specific branch
    def find_amount_available(self):
        cursor.execute("SELECT amount_available FROM books_in_branch WHERE book_number=%s and branch_number=%s", (self.book_number, self.branch_number))
        self.amount_available = cursor.fetchall()[0][0]

    # This method checks the availability of a specific book in a specific branch
    def book_availability(self):
        cursor.execute("SELECT amount_available FROM books_in_branch WHERE book_number=%s and branch_number=%s", (self.book_number, self.branch_number))
        res = cursor.fetchone()
        if res != None:
            return res[0] > 0
        return False

    # This method finds a branch # out of the email of the librarian who is currently connected to the system
    def find_branch_by_email(self):
        cursor.execute(
            "SELECT branch_number FROM librarian WHERE email_address=%s",
            (session["email"]))
        return cursor.fetchone()[0]

    # This method increases the amount available of specific book in specific branch by 1
    def update_amount_available(self):
        cursor.execute("UPDATE books_in_branch SET amount_available = amount_available + 1 WHERE book_number=%s", self.book_number)

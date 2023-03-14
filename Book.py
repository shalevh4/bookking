# This class contains all the relevant methods for book related actions
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session


class Book:
    # initiate the book object
    def __init__(self):
        self.book_number = 0
        self.book_name = ""
        self.author_name = ""
        self.year_published = 0
        self.publisher = ""

    # This method handles the insertion of a new book to the DB
    def insert_to_db(self):
        cursor.execute(
            "INSERT INTO book(book_number,book_name,author_name,year_published,publisher) VALUES(%s,%s,%s,%s,%s)", (self.book_number, self.book_name, self.author_name, self.year_published, self.publisher))
        connection.commit()

    # This method checks if the book is already exist in the DB
    def check_if_in_db(self):
        cursor.execute("SELECT book_number FROM book WHERE book_number=%s", self.book_number)
        return cursor.fetchall() != ()

    # This method finds the book number out of the book name
    def find_book_number(self):
        cursor.execute("SELECT book_number FROM book WHERE book_name=%s",
                       self.book_name)
        return cursor.fetchall()

    # This method finds the book number out of the author name
    def find_book_number_by_author(self):
        cursor.execute("SELECT book_number FROM book WHERE author_name=%s",
                       self.author_name)
        return cursor.fetchall()

    # This method finds the book name out of the book number
    def find_book_name_by_number(self):
        cursor.execute("SELECT book_name FROM book WHERE book_number=%s",
                       self.book_number)
        return cursor.fetchall()[0]

    # This method checks what books specific branch has
    def check_availability_in_branch(self):
        if len(self.book_number) >= 1:
            temp_list = []
            for number in self.book_number:
                self.book_number = number
                self.book_name = self.find_book_name_by_number()[0]
                cursor.execute(
                    "SELECT author_name,branch_name,phone_number,city,street,house_number,amount_available FROM books_in_branch bib JOIN branch br ON bib.branch_number = br.branch_number LEFT JOIN book b ON bib.book_number = b.book_number WHERE bib.book_number= %s", number)
                for row in cursor:
                    temp_list_b = list(row)
                    temp_list_b.insert(0, self.book_name)
                    temp_list.append(tuple(temp_list_b))
            return tuple(temp_list)
        else:
            return ()

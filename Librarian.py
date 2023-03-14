# This class contains all the relevant methods for the Librarian activity
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session
from People import People


class Librarian(People):
    # initiate the Librarian object
    def __init__(self):
        People.__init__(self)
        self.working_since = ""
        self.branch_number = 0

    # This method handles the login process of an existing librarian to the site
    def login(self):
        cursor.execute("SELECT email_address FROM librarian WHERE email_address=%s and password=%s",
                       (self.email, self.password))
        return cursor.fetchall()

    # This method checks if a librarian email is already exist in the DB
    def check_if_in_db(self):
        cursor.execute("SELECT email_address FROM librarian WHERE email_address=%s",
                       self.email)
        return cursor.fetchall() != ()

    # This method handles the insertion of a new librarian to the DB
    def insert_to_db(self):
        cursor.execute(
            "INSERT INTO librarian(email_address,first_name,last_name,phone_number,city,street,house_number,working_since,password,branch_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (self.email, self.first_name, self.last_name, self.phone_number, self.city, self.street, self.house_number, str(date.today()), self.password, self.branch_number))
        connection.commit()

    # This method returns the full name of the librarian by its email address
    def find_full_name(self):
        cursor.execute("SELECT first_name, last_name FROM librarian WHERE email_address = %s", self.email)
        result = cursor.fetchall()
        full_name = result[0][0] + ' ' + result[0][1]
        return full_name

    # This method finds the branch number by its name
    def find_branch_number_by_name(self):
        cursor.execute("SELECT branch_number FROM branch WHERE branch_name = %s", self.branch_number)
        return cursor.fetchall()[0]

# This class contains all the relevant methods for branch related actions
from db_connection import app, connection, cursor, Session


class Branch:
    # initiate the branch object
    def __init__(self):
        self.branch_number = 0
        self.branch_name = ""
        self.phone_number = ""
        self.city = ""
        self.street = ""
        self.house_num = 0

    # This method checks if the branch is already exist in the DB
    def check_if_in_db(self):
        cursor.execute("SELECT branch_number FROM branch WHERE branch_number=%s", self.branch_number)
        return cursor.fetchall() != ()

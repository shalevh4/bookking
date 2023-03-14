# This class contains all the relevant methods for borrow related actions
from datetime import datetime, date, timedelta
from db_connection import app, connection, cursor, Session


class Borrow:
    # initiate the borrow object
    def __init__(self):
        self.borrow_date = ''
        self.return_date = ''
        self.copy_number = 0
        self.customer_email = ''

    # This method handles the insertion of a new borrowing to the DB
    def insert_to_db(self):
        cursor.execute(
            "INSERT INTO borrow(borrow_date,return_date,copy_number,customer_email) VALUES(%s,%s,%s,%s)",
            (self.borrow_date, self.return_date, self.copy_number, self.customer_email))
        connection.commit()

    # This method returns a list of copies number that their borrow date expired
    def expired_borrow(self):
        cursor.execute("SELECT copy_number FROM copy WHERE current_status = 'borrowed' AND copy_number NOT IN (SELECT copy_number FROM borrow WHERE return_date >= CURRENT_DATE)")
        results = cursor.fetchall()
        return [row[0] for row in results]

    # This method is responsible to take care of borrow extension
    def extend_borrow(self):
        cursor.execute("SELECT return_date FROM borrow JOIN copy ON borrow.copy_number= copy.copy_number WHERE borrow.copy_number = %s AND return_date >= %s AND copy.current_status = 'borrowed'", (self.copy_number, datetime.now()))
        updated_return_date = cursor.fetchall()[0][0] + timedelta(days=7)
        cursor.execute("UPDATE borrow JOIN copy ON borrow.copy_number= copy.copy_number SET return_date = %s, extension_date = %s WHERE borrow.copy_number = %s AND return_date >= %s AND copy.current_status = 'borrowed'", (updated_return_date, datetime.now(), self.copy_number, datetime.now()))
        connection.commit()

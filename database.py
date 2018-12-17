import cymysql

"""!
@package database
"""

class DatabaseInspector:

    def connect(self, host, username, password, database_name):
        db = cymysql.connect(host=host, user=username, passwd=password, db=database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print
        "Database version : %s " % data
        # disconnect from server
        return db

    def read(self, host, username, password, database_name):
        db = self.connect(host, username, password, database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.

        query = """"""

        cursor.execute(query)
        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        print(data)
        # disconnect from server
        db.close()


if __name__ == '__main__':
    db = DatabaseInspector()
    db.read('127.0.0.1', 'hays0503', 'hays0503', 'librarydb')


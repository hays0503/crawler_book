import cymysql
from queryfactory import QueryFactory

"""!
@package database
"""


class DatabaseInspector:

    def connect(self, host, username, password, database_name):
        db = cymysql.connect (host=host, user=username, passwd=password, db=database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor ()
        # execute SQL query using execute() method.
        cursor.execute ("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone ()
        print
        "Database version : %s " % data
        # disconnect from server
        return db

    def read(self, host, username, password, database_name):
        db = cymysql.connect (host=host, user=username, passwd=password, db=database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor ()
        # execute SQL query using execute() method.

        #query = QueryFactory.add_row_in_table_books('Хуй', 1, 1, 1, 1, 1, 1, 'Пизда')
        query = QueryFactory.delete_by_id_book(8)
        print(query)
        cursor.execute("SET SQL_SAFE_UPDATES = 0;")
        cursor.execute(query)
        db.commit()
        # Fetch a single row using fetchone() method.
#        data = cursor.fetchall()
#        print(data)
        # disconnect from server
        db.close()

    def execute(self, query):
        return 0


if __name__ == '__main__':
    db = DatabaseInspector ()
    db.read ('127.0.0.1', 'hays0503', 'hays0503', 'librarydb')

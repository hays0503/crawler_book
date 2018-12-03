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
        db.close()

    def read(self, host, username, password, database_name):
        db = cymysql.connect(host=host, user=username, passwd=password, db=database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.

        query = """
        SELECT 
    `librarydb`.`books`.id_books,
    `librarydb`.`books`.name_book,
    `librarydb`.`books`.index_udc,
    `librarydb`.`books`.index_bbk,
    `librarydb`.`books`.isbn,
    GROUP_CONCAT(DISTINCT `librarydb`.`autor`.autor_record),
    GROUP_CONCAT(DISTINCT `librarydb`.`genre`.genre_record),
    GROUP_CONCAT(DISTINCT `librarydb`.`description`.description_record)
FROM
    `librarydb`.`books`
        JOIN
    `librarydb`.`autor_join_table` ON `librarydb`.`autor_join_table`.id_books = `librarydb`.`books`.id_books
        JOIN
    `librarydb`.`autor` ON `librarydb`.`autor`.id_autor = `librarydb`.`autor_join_table`.id_autor
        JOIN
    `librarydb`.`genre_join_table` ON `librarydb`.`genre_join_table`.id_books = `librarydb`.`books`.id_books
        JOIN
    `librarydb`.`genre` ON `librarydb`.`genre`.id_genre = `librarydb`.`genre_join_table`.id_genre
        JOIN
    `librarydb`.`description` ON `librarydb`.`description`.id_description = `librarydb`.`books`.id_books
GROUP BY `librarydb`.`books`.id_books;"""

        cursor.execute(query)
        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        print(data)
        # disconnect from server
        db.close()


if __name__ == '__main__':
    db = DatabaseInspector()
    db.read('127.0.0.1', 'hays0503', 'hays0503', 'librarydb')


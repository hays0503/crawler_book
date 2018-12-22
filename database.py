import cymysql
from queryfactory import QueryFactory

"""!
@package database
"""


class DatabaseInspector:

    host = ""
    username = ""
    password = ""
    database_name = ""

    def connect(self, host, username, password, database_name):
        self.host = host, self.username = username, self.password = password, self.database_name = database_name
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

    def read(self):
        db = cymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.

        index_book = 0
        index_author = 0
        index_genre = 0
        name_book = 'Хуй'
        name_genre = 'Хуйня внеземная'
        author = 'Пизда Ивановна'

        # Добавление книги
        query = QueryFactory.add_row_in_table_books(name_book, 1, 1, 1,
                                                    1, 1,
                                                    '1-2-3-4-5')
        cursor.execute(query)
        db.commit()

        # Добавление авторов
        query = QueryFactory.add_row_in_table_author(author)
        print(query)
        cursor.execute(query)
        db.commit()

        # Взять индекс книги по названию
        query = QueryFactory.search_by_name_book(name_book)
        print(query)
        cursor.execute(query)
        index_book = cursor.fetchall()[0][0]
        print(index_book)
        db.commit()

        # Взять индекс автора по имени
        query = QueryFactory.search_by_name_author(author)
        print(query)
        cursor.execute(query)
        index_author = cursor.fetchall()[0][0]
        print(index_author)
        db.commit()

        # Cвязать авторов с книгой
        query = QueryFactory.add_row_in_author_join_table(index_book, index_author)
        print(query)
        cursor.execute(query)
        db.commit()

        # Добавление жанр
        query = QueryFactory.add_row_in_table_genre(name_genre)
        print(query)
        cursor.execute(query)
        db.commit()

        # Взять индекс жанра по названию
        query = QueryFactory.search_by_name_genre(name_genre)
        print(query)
        cursor.execute(query)
        index_genre = cursor.fetchall()[0][0]
        print(index_genre)
        db.commit()

        # Cвязать жанра с книгой
        query = QueryFactory.add_row_in_genre_join_table(index_book, index_genre)
        print(query)
        cursor.execute(query)
        db.commit()

        query = QueryFactory.add_row_in_table_description("Ну хуй знает что тут можно написать")
        print(query)
        cursor.execute(query)
        db.commit()

        # Fetch a single row using fetchone() method.
        #        data = cursor.fetchall()
        #        print(data)
        # disconnect from server
        db.close()

    def execute(self, query):
        db = cymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.database_name)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute(query)
        print(cursor.fetchall)
        return 0

    def add_book(self, name_book="", name_genre="", author="", isbn="", descriprion=""):
            index_book = 0
            index_author = 0
            index_genre = 0

            db = cymysql.connect(host=self.host, user=self.username, passwd=self.password, db=self.database_name)
            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # Добавление книги          #number_of_pages_book
            query = QueryFactory.add_row_in_table_books(name_book, 1, 1, 1,
                                                        1, 1,
                                                        isbn)
            cursor.execute(query)
            db.commit()

            # Добавление авторов
            query = QueryFactory.add_row_in_table_author(author)
            print(query)
            cursor.execute(query)
            db.commit()

            # Взять индекс книги по названию
            query = QueryFactory.search_by_name_book(name_book)
            print(query)
            cursor.execute(query)
            index_book = cursor.fetchall()[0][0]
            print(index_book)
            db.commit()

            # Взять индекс автора по имени
            query = QueryFactory.search_by_name_author(author)
            print(query)
            cursor.execute(query)
            index_author = cursor.fetchall()[0][0]
            print(index_author)
            db.commit()

            # Cвязать авторов с книгой
            query = QueryFactory.add_row_in_author_join_table(index_book, index_author)
            print(query)
            cursor.execute(query)
            db.commit()

            # Добавление жанр
            query = QueryFactory.add_row_in_table_genre(name_genre)
            print(query)
            cursor.execute(query)
            db.commit()

            # Взять индекс жанра по названию
            query = QueryFactory.search_by_name_genre(name_genre)
            print(query)
            cursor.execute(query)
            index_genre = cursor.fetchall()[0][0]
            print(index_genre)
            db.commit()

            # Cвязать жанра с книгой
            query = QueryFactory.add_row_in_genre_join_table(index_book, index_genre)
            print(query)
            cursor.execute(query)
            db.commit()

            query = QueryFactory.add_row_in_table_description(descriprion)
            print(query)
            cursor.execute(query)
            db.commit()


if __name__ == '__main__':
    db = DatabaseInspector()
    db.read('127.0.0.1', 'hays0503', 'hays0503', 'librarydb')
    db.execute(QueryFactory.search_by_binding_book('мягкая обложка'))

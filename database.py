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
    db = None

    def connect(self, host, username, password, database_name):
        self.host = host
        self.username = username
        self.password = password
        self.database_name = database_name
        self.db = cymysql.connect(host=host, user=username, passwd=password, db=database_name)
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print
        "Database version : %s " % data
        # disconnect from server
        return self.db

    def read(self):
        if self.db is None:
            return "database not connection"
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()
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
        self.db.commit()

        # Добавление авторов
        query = QueryFactory.add_row_in_table_author(author)
        print(query)
        cursor.execute(query)
        self.db.commit()

        # Взять индекс книги по названию
        query = QueryFactory.search_by_name_book(name_book)
        print(query)
        cursor.execute(query)
        index_book = cursor.fetchall()[0][0]
        print(index_book)
        self.db.commit()

        # Взять индекс автора по имени
        query = QueryFactory.search_by_name_author(author)
        print(query)
        cursor.execute(query)
        index_author = cursor.fetchall()[0][0]
        print(index_author)
        self.db.commit()

        # Cвязать авторов с книгой
        query = QueryFactory.add_row_in_author_join_table(index_book, index_author)
        print(query)
        cursor.execute(query)
        self.db.commit()

        # Добавление жанр
        query = QueryFactory.add_row_in_table_genre(name_genre)
        print(query)
        cursor.execute(query)
        self.db.commit()

        # Взять индекс жанра по названию
        query = QueryFactory.search_by_name_genre(name_genre)
        print(query)
        cursor.execute(query)
        index_genre = cursor.fetchall()[0][0]
        print(index_genre)
        self.db.commit()

        # Cвязать жанра с книгой
        query = QueryFactory.add_row_in_genre_join_table(index_book, index_genre)
        print(query)
        cursor.execute(query)
        self.db.commit()

        query = QueryFactory.add_row_in_table_description("Ну хуй знает что тут можно написать")
        print(query)
        cursor.execute(query)
        self.db.commit()

        # Fetch a single row using fetchone() method.
        #        data = cursor.fetchall()
        #        print(data)
        # disconnect from server
        self.db.close()

    def execute(self, query):
        if self.db is None:
            return "database not connection"
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()
        # execute SQL query using execute() method.
        print(query)
        try:
            cursor.execute(query)
            self.db.commit()
            data = cursor.fetchall()
        except cymysql.err.IntegrityError:
            return
        return data

    def what_is_index(self, query_object):
        if self.db is None:
            return "database not connection"
        return self.execute(query_object)[0][0]

    def add_book(self, authors, name_genre, name_book="",
                 isbn="", description="", number_of_pages_book=0,
                 release_date=0, book_binding_type="", index_udc=0, index_bbk=0):

        if self.db is None:
            return "database not connection"

        # prepare a cursor object using cursor() method
        cursor = self.db.cursor()

        index_book_binding_type = self.what_is_index(QueryFactory.search_by_binding_book(book_binding_type))

        # Добавление книги
        self.execute(QueryFactory.add_row_in_table_books(name_book=name_book,
                                                         number_of_pages_book=number_of_pages_book,
                                                         index_book_binding_type=index_book_binding_type,
                                                         release_date_book=release_date,
                                                         index_udc=index_udc,
                                                         index_bbk=index_bbk,
                                                         isbn=isbn))

        # Добавление авторов
        for author_book in authors:
            self.execute(QueryFactory.add_row_in_table_author(author_book))

        # Взять индекс книги по названию
        index_book = self.what_is_index(QueryFactory.search_by_name_book(name_book))

        # Взять индекс автора по имени
        index_author = []
        for author_book in authors:
            index_author.append(self.what_is_index(QueryFactory.search_by_name_author(author_book)))

        # Cвязать авторов с книгой
        for author_book in index_author:
            self.execute(QueryFactory.add_row_in_author_join_table(index_book, author_book))

        # Добавление жанр
        for genre in name_genre:
            self.execute(QueryFactory.add_row_in_table_genre(genre))

        # Взять индекс жанра по названию
        index_genre = []
        for genre in name_genre:
            index_genre.append(self.what_is_index(QueryFactory.search_by_name_genre(genre)))

        # Cвязать жанра с книгой
        for genre in index_genre:
            self.execute(QueryFactory.add_row_in_genre_join_table(index_book, genre))

        # Добавить описание книге
        self.execute(QueryFactory.add_row_in_table_description(description))


if __name__ == '__main__':
    db = DatabaseInspector()
    db.connect('127.0.0.1', 'hays0503', 'hays0503', 'librarydb')

    name_book = 'Хуй'
    name_genre = ['Хуйня внеземная']
    author = ['Пизда Ивановна', 'Владимир серый хуй']
    description = "description description description description"
    isbn = "12345"
    index_bbk = 1
    index_udc = 1
    number_of_pages_book = 200
    release_date = 2007
    book_binding_type = "мягкая обложка"
    db.add_book(name_book=name_book,
                name_genre=name_genre,
                authors=author,
                isbn=isbn,
                index_udc=index_udc,
                index_bbk=index_bbk,
                description=description,
                number_of_pages_book=number_of_pages_book,
                release_date=release_date,
                book_binding_type=book_binding_type)

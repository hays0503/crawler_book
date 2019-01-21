"""!
@package crawler
"""

from tableReader import TableInspector
from downloader import InfoByPost
from database import DatabaseInspector
from filesysteamdb import fsdb
from queryfactory import QueryFactory
import cProfile

class Crawler():
    """!
        @description Web + offline crawler book info
    """

    object_table_inspector = None
    object_database_inspector = DatabaseInspector()
    searth_by_post = InfoByPost()

    object_fsdb = fsdb()
    object_fsdb.connect(
        '127.0.0.1',
        'hays0503',
        'hays0503',
        'librarydb'
    )
    object_fsdb.add_list_file()
    """for file in object_fsdb.list_file:
        object_fsdb.update(file, "0")
    """
    info_by_book = {
        "name_book": "",
        "number_of_pages_book": 0,
        "book_binding_type": "",
            "release_date_book": 0,
            "index_udc": "0",
            "index_bbk": "0",
        "publisher": "",
        "description": "",
            "author": [],
            "genre": [],
            "isbn": ""
    }
    books = []

    def add_books(self):
        self.object_database_inspector.connect(
            '127.0.0.1',
            'hays0503',
            'hays0503',
            'librarydb'
        )
        for iterator in self.books:
            self.object_database_inspector.add_book(
                name_book = iterator["name_book"],
                number_of_pages_book = iterator["number_of_pages_book"],
                book_binding_type = iterator["book_binding_type"],
                release_date = iterator["release_date_book"],
                index_udc = iterator["index_udc"],
                index_bbk = iterator["index_bbk"],
                publisher = iterator["publisher"],
                isbn = iterator["isbn"],
                description = iterator["description"],
                authors = iterator["author"],
                name_genre = iterator["genre"]
            )

    def add_book(self, iterator):
        self.object_database_inspector.connect(
            '127.0.0.1',
            'hays0503',
            'hays0503',
            'librarydb'
        )

        self.object_database_inspector.add_book(
            name_book = iterator["name_book"],
            number_of_pages_book = iterator["number_of_pages_book"],
            book_binding_type = iterator["book_binding_type"],
            release_date = iterator["release_date_book"],
            index_udc = iterator["index_udc"],
            index_bbk = iterator["index_bbk"],
            publisher = iterator["publisher"],
            isbn = iterator["isbn"],
            description = iterator["description"],
            authors = iterator["author"],
            name_genre = iterator["genre"]
        )

    def cache(self):
        self.object_database_inspector.connect(
            '127.0.0.1',
            'hays0503',
            'hays0503',
            'librarydb'
        )
        list = self.object_database_inspector.execute(QueryFactory.show_all())
        for item in list:
            self.object_database_inspector.execute(
                QueryFactory.add_row_in_table_cache(item[0], item[1], item[2],
                                                    item[3], item[4], item[5],
                                                    item[6], item[7], item[8],
                                                    item[9], item[10], item[11])
            )

    def change_author_null(self):
        self.object_database_inspector.connect(
            '127.0.0.1',
            'hays0503',
            'hays0503',
            'librarydb'
        )
        list = self.object_database_inspector.execute(QueryFactory.get_author_null_id())
        for item in list:
            self.object_database_inspector.execute(
                QueryFactory.add_row_in_author_join_table(item[0], 1)
            )

    def change_genre_null(self):
        self.object_database_inspector.connect(
            '127.0.0.1',
            'hays0503',
            'hays0503',
            'librarydb'
        )
        list = self.object_database_inspector.execute(QueryFactory.get_genre_null_id())
        for item in list:
            self.object_database_inspector.execute(
                QueryFactory.add_row_in_genre_join_table(item[0], 1)
            )


    def start(self):
        for file in self.object_fsdb.list_file:
            self.object_table_inspector = None
            self.object_table_inspector = TableInspector(patch_to_file = file)
            begin_row = self.object_fsdb.start_row_file(file_name = file)
            print(begin_row)
            end_row = len(self.object_table_inspector.other_description)
            for iterator in range(end_row):
                iterator = begin_row
                print('--------------')
                print(str(iterator) + " : " + str(end_row)+' '+file)
                print(self.object_table_inspector.url(iterator))
                self.searth_by_post.info(self.object_table_inspector.url(iterator))
                self.info_by_book["name_book"] = self.object_table_inspector.name_book(iterator)
                self.info_by_book["number_of_pages_book"] = self.object_table_inspector.number_of_pages_book(iterator)
                self.info_by_book["book_binding_type"] = self.object_table_inspector.book_binding_type(iterator)
                self.info_by_book["release_date_book"] = self.searth_by_post.release_year_data
                self.info_by_book["index_udc"] = "1"
                self.info_by_book["index_bbk"] = "1"
                self.info_by_book["publisher"] = self.object_table_inspector.publisher_book(iterator)
                self.info_by_book["isbn"] = self.searth_by_post.isbn
                self.info_by_book["description"] = self.searth_by_post.description
                self.info_by_book["author"] = self.searth_by_post.author
                self.info_by_book["genre"] = self.searth_by_post.genre
                self.add_book(self.info_by_book.copy())
                self.object_fsdb.update(file, iterator)
                self.info_by_book.clear()
                begin_row = iterator + 1
                if begin_row == end_row:
                    break


if __name__ == '__main__':
    object_crawler = Crawler()
    object_crawler.start()


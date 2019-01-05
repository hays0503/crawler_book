"""!
@package crawler
"""

from tableReader import TableInspector
from downloader import InfoByPost
from database import DatabaseInspector
import cProfile

class Crawler():
    """!
        @description Web + offline crawler book info
    """

    object_table_inspector = TableInspector(patch_to_file="prices_s2.xlsx")
    object_database_inspector = DatabaseInspector()
    searth_by_post = InfoByPost()


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

    def add_book(self):
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

    def start(self):
        num_books = len(self.object_table_inspector.other_description)
        for iterator in range(num_books):
            self.searth_by_post.info(self.object_table_inspector.url(iterator))
            self.info_by_book["name_book"] = self.object_table_inspector.name_book(iterator)
            self.info_by_book["number_of_pages_book"] = self.object_table_inspector.number_of_pages_book(iterator)
            self.info_by_book["book_binding_type"] = self.object_table_inspector.book_binding_type(iterator)
            self.info_by_book["release_date_book"] = self.self.searth_by_post.
            self.info_by_book["index_udc"] = "1"
            self.info_by_book["index_bbk"] = "1"
            self.info_by_book["publisher"] = self.object_table_inspector.publisher_book(iterator)
            self.info_by_book["isbn"] = self.searth_by_post.isbn
            self.info_by_book["description"] = self.searth_by_post.description
            self.info_by_book["author"] = self.searth_by_post.author
            self.info_by_book["genre"] = self.searth_by_post.genre
            print(str(iterator) + " : " + str(range(num_books)))
            print(self.object_table_inspector.url(iterator))
            self.books.append(self.info_by_book.copy())
            self.info_by_book.clear()
        self.add_book()

if __name__ == '__main__':
    object_crawler = Crawler()
    object_crawler.start()


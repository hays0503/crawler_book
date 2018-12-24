"""!
@package crawler
"""

from tableReader import TableInspector
from downloader import InfoByPost

class Crawler():
    """!
        @description Web + offline crawler book info
    """

    TableInspector = TableInspector(patch_to_file="prices_s2.xlsx")
    searth_by_post = InfoByPost()

    InfoByBook = {
        "name_book": "",
        "number_of_pages_book": 0,
        "index_book_binding_type": 0,
        "release_date_book": 0,
        "index_udc": 0,
        "index_bbk": 0,
        "index_publisher": 0,
        "isbn": ""
    }


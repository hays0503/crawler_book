import requests
from bs4 import BeautifulSoup
import re

"""!
@package infobypost
"""


class InfoByPost:
    """!
    @brief Parser information about the post
    @brief Парсер информации о посте
    """

    isbn = None
    description = None
    author = None
    genre = None


    def __isbn(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all(string=re.compile(r"(\d\d\d-\d\d\d-\d\d-\d\d\d\d-\d|\d-\d\d\d\d\d-\d\d\d-(\d|\w))"))
        self.isbn = last_links

    def __description(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all('span', itemprop="description")
        self.description = last_links[0].text

    def __author(self, data):
        """!
        @brief Parser author(s) of the book
        @brief Парсер автора(ов) книги
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find('div', {"class": "p-10 author-block"})

        soup = BeautifulSoup(str(last_links), 'html.parser')
        last_links = soup.find_all('b', itemprop="name")
        list_autor = []
        for name_autor in last_links:
            list_autor.append(name_autor.text)
        self.author = list_autor

    def __genre(self, data):
        """!
        @brief Parser author(s) of the book
        @brief Парсер автора(ов) книги
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find('div', {"class": "krohi"})

        soup = BeautifulSoup(str(last_links), 'html.parser')
        last_links = soup.find_all('span', {"property": "name"})
        list_autor = []
        for name_autor in last_links:
            list_autor.append(name_autor.text)
        self.genre = list_autor

    def info(self, url):
        """!
        @brief Compiling all information about the post
        @brief Компиляция всего информации об посте
        @param [in] str url
        @return str
        """
        rc = requests.get(url)
        data = rc.text
        self.__isbn(data)
        self.__description(data)
        self.__author(data)
        self.__genre(data)

"""
if __name__ == '__main__':
    info = InfoByPost()
    info.info("https://www.flip.kz/catalog?prod=35")
"""
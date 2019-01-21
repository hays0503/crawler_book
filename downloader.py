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
    release_year_data = None


    def __isbn(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        regexp = r"(\d-\d\d\d\d-\d\d\d\d-(\d|\w)|" \
                 r"\d-\d\d-\d\d\d\d\d\d-\d|" \
                 r"\d\d\d-\d\d\d-\d\d\d-\d\d\d-\d|" \
                 r"\d\d\d\d\d\d\d\d\d\d\d\d\d|" \
                 r"\d\d\d-\d-\d\d\d\d\d\d\d-\d-\d|" \
                 r"\d-\d\d\d-\d\d\d\d\d-\d|" \
                 r"\d-\d\d\d\d-\d\d\d\d-\d|" \
                 r"\d\d\d-\d-\d\d-\d\d\d\d\d\d-\d|" \
                 r"\d\d\d-\d-\d\d\d\d\d\d-\d\d-\d|" \
                 r"\d\d\d-\d\d\d\d-\d\d-\d|" \
                 r"\d\d\d-\d-\d\d\d-\d\d\d\d\d-\d|" \
                 r"\d\d\d-\d-\d\d-\d\d\d\d\d\d-\d|" \
                 r"\d\d\d-\d\d\d-\d\d\d\d\d-\d-\d|" \
                 r"\d\d\d-\d-\d\d\d-\d\d\d\d-\d|" \
                 r"\d\d\d-\d\d\d-\d\d-\d\d\d\d-\d|" \
                 r"\d\d\d-\d-\d\d\d\d-\d\d\d\d-\d|" \
                 r"\d-\d\d\d-\d\d\d\d\d-(\d|\w)|" \
                 r"\d-\d\d\d\d\d-\d\d\d-(\d|\w))"
        last_links = soup.find(string=re.compile(regexp))
        text = last_links
        self.isbn = re.sub(" ","",text)

    def __description(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all('span', itemprop="description")
        if len(last_links) == 0:
            self.description = " "
            return
        text = last_links[0].text
        self.description = re.sub("'","",text)

    def __release_year_data(self, data):
        """!
        @brief release date book Parser
        @brief Парсер даты выпуска
        @param [in] str url
        @return str
        """
        try:
            soup = BeautifulSoup(''.join(data), 'html.parser')
            if soup.find(string=re.compile(",\s\d\d\d\d\sг")) is not None:
                last_links = soup.find(string=re.compile(",\s\d\d\d\d\sг")).split(' ')
                print(last_links)
                if str(last_links[1]).isdigit():
                    self.release_year_data = int(last_links[1])
            else:
                last_links = soup.find(string = re.compile("\w\s\d\d\d\d\sг"))
                print(last_links)
                if last_links is not None:
                    self.release_year_data = int(str(last_links).split(' ')[3])
            if self.release_year_data is None:
                self.release_year_data = 0
        except ValueError:
            self.release_year_data = 0

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
            text = name_autor.text
            list_autor.append(re.sub("'","",text))
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
        for name_genre in last_links:
            text = name_genre.text
            list_autor.append(re.sub("'","",text))
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
        self.__release_year_data(data)
        self.__isbn(data)
        self.__description(data)
        self.__author(data)
        self.__genre(data)

"""
if __name__ == '__main__':
    info = InfoByPost()
    info.info("https://www.flip.kz/catalog?prod=43304")
"""
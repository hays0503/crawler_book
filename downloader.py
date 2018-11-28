import requests
from bs4 import BeautifulSoup
import re

"""!
@package infobypost
"""


class infoByPost():
    """!
    @brief Parser information about the post
    @brief Парсер информации о посте
    """

    def isbn(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """

        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all(string=re.compile("\d\d\d-\d\d\d-\d\d-\d\d\d\d-\d"))
        print(last_links)

    def description(self, data):
        """!
        @brief Isbn Parser
        @brief Парсер isbn
        @param [in] str url
        @return str
        """
        soup = BeautifulSoup(''.join(data), 'html.parser')
        last_links = soup.find_all('span', itemprop="description")
        print(last_links[0].text)


    def info(self, url):
        """!
        @brief Compiling all information about the post
        @brief Компиляция всего информации об посте
        @param [in] str url
        @return str
        """
        rc = requests.get(url)
        data = rc.text
        self.isbn(data)
        self.description(data)


if __name__ == '__main__':
    info = infoByPost()
    info.info("https://www.flip.kz/catalog?prod=1237852")

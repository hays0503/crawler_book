"""!
@package queryfactory
"""


class QueryFactory (object):
    """!
        @brief Query factory
        @brief Фабрика запросов
    """

    @staticmethod
    def show_all():
        return """
        SELECT 
            `librarydb`.`books`.id_books,
            `librarydb`.`books`.name_book,
            GROUP_CONCAT(DISTINCT `librarydb`.`book_binding_type`.binding_type),
            `librarydb`.`books`.index_udc,
            `librarydb`.`books`.index_bbk,
            `librarydb`.`books`.isbn,
            GROUP_CONCAT(DISTINCT `librarydb`.`author`.author_record),
            GROUP_CONCAT(DISTINCT `librarydb`.`genre`.genre_record),
            GROUP_CONCAT(DISTINCT `librarydb`.`description`.description_record)
        FROM
            `librarydb`.`books`
                JOIN
            `librarydb`.`author_join_table` ON `librarydb`.`author_join_table`.id_books = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`author` ON `librarydb`.`author`.id_author = `librarydb`.`author_join_table`.id_author
                JOIN
            `librarydb`.`genre_join_table` ON `librarydb`.`genre_join_table`.id_books = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`genre` ON `librarydb`.`genre`.id_genre = `librarydb`.`genre_join_table`.id_genre
                JOIN
            `librarydb`.`description` ON `librarydb`.`description`.id_description = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type = `librarydb`.`books`.index_book_binding_type
        GROUP BY `librarydb`.`books`.id_books;
        """

    @staticmethod
    def search_by_id_book(id_book):
        query = """
        SELECT 
            `librarydb`.`books`.id_books,
            `librarydb`.`books`.name_book,
            GROUP_CONCAT(DISTINCT `librarydb`.`book_binding_type`.binding_type),
            `librarydb`.`books`.index_udc,
            `librarydb`.`books`.index_bbk,
            `librarydb`.`books`.isbn,
            GROUP_CONCAT(DISTINCT `librarydb`.`author`.author_record),
            GROUP_CONCAT(DISTINCT `librarydb`.`genre`.genre_record),
            GROUP_CONCAT(DISTINCT `librarydb`.`description`.description_record)
        FROM
            `librarydb`.`books`
                JOIN
            `librarydb`.`author_join_table` ON `librarydb`.`author_join_table`.id_books = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`author` ON `librarydb`.`author`.id_author = `librarydb`.`author_join_table`.id_author
                JOIN
            `librarydb`.`genre_join_table` ON `librarydb`.`genre_join_table`.id_books = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`genre` ON `librarydb`.`genre`.id_genre = `librarydb`.`genre_join_table`.id_genre
                JOIN
            `librarydb`.`description` ON `librarydb`.`description`.id_description = `librarydb`.`books`.id_books
                JOIN
            `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type = `librarydb`.`books`.index_book_binding_type
        WHERE
            `librarydb`.`books`.id_books IN (SELECT 
                    librarydb.genre_join_table.id_books
                FROM
                    librarydb.genre_join_table
                WHERE
                    librarydb.genre_join_table.id_genre = '%i')
        GROUP BY `librarydb`.`books`.id_books;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_book(id_book):
        query = """
        SET SQL_SAFE_UPDATES = 0;
        
        DELETE FROM `librarydb`.`author_join_table` 
        WHERE
            `librarydb`.`author_join_table`.id_books = '%i';
        
        DELETE FROM `librarydb`.`genre_join_table` 
        WHERE
            `librarydb`.`genre_join_table`.id_books = '%i';
        
        DELETE FROM `librarydb`.`bbk` 
        WHERE
            `librarydb`.`bbk`.id_bbk = '%i';
        
        DELETE FROM `librarydb`.`udc` 
        WHERE
            `librarydb`.`udc`.id_udc = '%i';
        
        DELETE FROM `librarydb`.`description` 
        WHERE
            `librarydb`.`description`.id_description = '%i';
        
        DELETE FROM `librarydb`.`books` 
        WHERE
            `librarydb`.`books`.id_books = '%i';
        """ % (id_book, id_book, id_book, id_book, id_book, id_book)
        return query

    @staticmethod
    def add_row_in_table_genre(author_name):
        if type (author_name) is not list:
            query = "INSERT INTO `librarydb`.`genre`(`genre_record`) VALUES ('%s');" % author_name
        else:
            query = "INSERT INTO `librarydb`.`genre`(`genre_record`) VALUES"
            query += " ('" + "'),('".join (author) + "');"
        return query

    @staticmethod
    def add_row_in_table_bbk(author_name):
        if type (author_name) is not list:
            query = "INSERT INTO `librarydb`.`bbk`(`bbk_record`) VALUES ('%s');" % author_name
        else:
            query = "INSERT INTO `librarydb`.`bbk`(`bbk_record`) VALUES"
            query += " ('" + "'),('".join (author) + "');"
        return query

    @staticmethod
    def add_row_in_table_udc(author_name):
        if type (author_name) is not list:
            query = "INSERT INTO `librarydb`.`udc`(`udc_record`) VALUES ('%s');" % author_name
        else:
            query = "INSERT INTO `librarydb`.`udc`(`udc_record`) VALUES"
            query += " ('" + "'),('".join (author) + "');"
        return query

    @staticmethod
    def add_row_in_table_description(author_name):
        if type (author_name) is not list:
            query = "INSERT INTO `librarydb`.`description`(`description_record`) VALUES ('%s');" % author_name
        else:
            query = "INSERT INTO `librarydb`.`description`(`description_record`) VALUES"
            query += " ('" + "'),('".join (author) + "');"
        return query

    @staticmethod
    def add_row_in_table_books(name_book, number_of_pages_book,
                               index_book_binding_type, release_date_book,
                               index_udc, index_bbk, index_description, isbn):
        if type (name_book) is not list:
            query = "INSERT INTO `librarydb`.`description`" \
                    "`(`name_book`,`number_of_pages_book`," \
                    "`index_book_binding_type`,`release_date_book`," \
                    "`index_udc`,`index_bbk`,`index_description`,`isbn`)" \
                    " VALUES ('%s', %s, %s, %s, %s, %s, %s, '%s');" \
                    % (name_book, str (number_of_pages_book), str (index_book_binding_type),
                       str (release_date_book), str (index_udc), str (index_bbk), str (index_description), isbn)
        else:
            query = "INSERT INTO `librarydb`.`description`" \
                    "(`name_book`,`number_of_pages_book`," \
                    "`index_book_binding_type`,`release_date_book`," \
                    "`index_udc`,`index_bbk`,`index_description`,`isbn`)" \
                    " VALUES"
            iterator = 0
            while iterator < len(name_book):
                query += "('" + name_book[iterator] + "'," + str(number_of_pages_book[iterator]) + "," +\
                         str(index_book_binding_type[iterator]) + "," + str(release_date_book[iterator]) + "," +\
                         str(index_udc[iterator]) + "," + str(index_bbk[iterator]) + "," +\
                         str(index_description[iterator]) + ",'" + isbn[iterator] + "')"
                iterator += 1
                if iterator < len(name_book):
                    query += ","
                query += ";"
        return query

    @staticmethod
    def add_row_in_author_join_table(id_books, id_author):
        if type(id_books) is not list:
            query = "INSERT INTO `librarydb`.`author_join_table`" \
                    "(`id_books`,`id_author`)" \
                    " VALUES (%s, %s);" \
                    % (str(id_books), str(id_author))
        else:
            query = "INSERT INTO `librarydb`.`author_join_table`" \
                    "(`id_books`,`id_author`)" \
                    " VALUES"
            iterator = 0
            while iterator < len(id_books):
                query += "(" + str(id_books[iterator]) + "," + str(id_author[iterator]) + ")"
                iterator += 1
                if iterator < len(id_books):
                    query += ","
            query += ";"
        return query

    @staticmethod
    def add_row_in_genre_join_table(id_books, id_genre):
        if type(id_books) is not list:
            query = "INSERT INTO `librarydb`.`genre_join_table`" \
                    "(`id_books`,`id_genre`)" \
                    " VALUES (%s, %s);" \
                    % (str(id_books), str(id_genre))
        else:
            query = "INSERT INTO `librarydb`.`genre_join_table`" \
                    "(`id_books`,`id_genre`)" \
                    " VALUES"
            iterator = 0
            while iterator < len(id_books):
                query += "(" + str(id_books[iterator]) + "," + str(id_genre[iterator]) + ")"
                iterator += 1
                if iterator < len(id_books):
                    query += ","
            query += ";"
        return query


if __name__ == '__main__':
    name_book = 'aaa'
    number_of_pages_book = 1
    index_book_binding_type = 1
    release_date_book = 1
    index_udc = 1
    index_bbk = 1
    index_description = 1
    isbn = 'aaa'
    author = 'ddd'
    print(type(author) is list)
    print(QueryFactory.add_row_in_genre_join_table([1, 2], [3, 4]))
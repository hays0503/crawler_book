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
        query ="""
            SELECT 
                `librarydb`.`books`.id_books,
                `librarydb`.`books`.name_book,
                GROUP_CONCAT(DISTINCT `librarydb`.`author`.author_record),
                GROUP_CONCAT(DISTINCT `librarydb`.`genre`.genre_record),
                `librarydb`.`bbk`.bbk_record,
                `librarydb`.`udc`.udc_record,
                `librarydb`.`books`.isbn,
                `librarydb`.`publisher`.publisher_record,
                `librarydb`.`books`.number_of_pages_book,
                GROUP_CONCAT(DISTINCT `librarydb`.`book_binding_type`.binding_type),
                `librarydb`.`books`.description_record,
                `librarydb`.`books`.`release_date_book`
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
                `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type = `librarydb`.`books`.index_book_binding_type
                    JOIN
                `librarydb`.`publisher` ON `librarydb`.`publisher`.id_publisher = `librarydb`.`books`.index_publisher
                    JOIN
                `librarydb`.`udc` ON `librarydb`.`udc`.id_udc = `librarydb`.`books`.index_udc
                    JOIN
                `librarydb`.`bbk` ON `librarydb`.`bbk`.id_bbk = `librarydb`.`books`.index_bbk
            GROUP BY `librarydb`.`books`.id_books;
        """
        return query

    @staticmethod
    def search_by_id_book(id_book):
        query = """SELECT 
                `librarydb`.`books`.id_books,
                `librarydb`.`books`.name_book,
                GROUP_CONCAT(DISTINCT `librarydb`.`book_binding_type`.binding_type),
                `librarydb`.`udc`.udc_record,
                `librarydb`.`bbk`.bbk_record,
                `librarydb`.`books`.isbn,
                `librarydb`.`publisher`.publisher_record,
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
                `librarydb`.`description` ON `librarydb`.`description`.id_books = `librarydb`.`books`.id_books
                    JOIN
                `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type = `librarydb`.`books`.index_book_binding_type
                    JOIN
                `librarydb`.`publisher` ON `librarydb`.`publisher`.id_publisher = `librarydb`.`books`.index_publisher
                    JOIN
                `librarydb`.`udc` ON `librarydb`.`udc`.id_udc = `librarydb`.`books`.index_udc
                    JOIN
                `librarydb`.`bbk` ON `librarydb`.`bbk`.id_bbk = `librarydb`.`books`.index_bbk
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
    def search_by_file_name(file_name):
        query = """
          SELECT `librarydb`.`filetables`.number_of_row
          FROM
              `librarydb`.`filetables`
          WHERE
              `librarydb`.`filetables`.file_name = '%s'
          """ % file_name
        return query

    @staticmethod
    def search_by_name_book(name_book):
        query = """
        SELECT `librarydb`.`books`.id_books
            
        FROM
            `librarydb`.`books`
        WHERE
            `librarydb`.`books`.name_book = '%s'
        """ % name_book
        return query

    @staticmethod
    def search_by_binding_book(name_binding):
        query = """
        SELECT `librarydb`.`book_binding_type`.id_book_binding_type

        FROM
            `librarydb`.`book_binding_type`
        WHERE
            `librarydb`.`book_binding_type`.`binding_type` = '%s'
        """ % name_binding
        return query

    @staticmethod
    def search_by_publisher_name(publisher_name):
        query = """
        SELECT `librarydb`.`publisher`.id_publisher

        FROM
            `librarydb`.`publisher`
        WHERE
            `librarydb`.`publisher`.`publisher_record` = '%s'
        """ % publisher_name
        return query

    @staticmethod
    def search_by_name_author(name_book):
        query = """
        SELECT `librarydb`.`author`.id_author

        FROM
            `librarydb`.`author`
        WHERE
            `librarydb`.`author`.author_record = '%s'
        """ % name_book
        return query

    @staticmethod
    def search_by_name_genre(name_genre):
        query = """
        SELECT `librarydb`.`genre`.id_genre

        FROM
            `librarydb`.`genre`
        WHERE
            `librarydb`.`genre`.genre_record = '%s'
        """ % name_genre
        return query

    @staticmethod
    def delete_by_id_book(id_book):
        query = """
        DELETE FROM `librarydb`.`books` 
        WHERE
            `librarydb`.`books`.id_books = %i;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_author_join_table(id_book):
        query = """
        DELETE FROM `librarydb`.`author_join_table` 
        WHERE
            `librarydb`.`author_join_table`.id_books = %i;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_genre_join_table(id_book):
        query = """
        DELETE FROM `librarydb`.`genre_join_table` 
        WHERE
            `librarydb`.`genre_join_table`.id_books = %i;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_bbk(id_book):
        query = """
        DELETE FROM `librarydb`.`bbk` 
        WHERE
            `librarydb`.`bbk`.id_bbk = %i;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_udc(id_book):
        query = """
        DELETE FROM `librarydb`.`udc` 
        WHERE
            `librarydb`.`udc`.id_udc = %i;
        """ % id_book
        return query

    @staticmethod
    def delete_by_id_description(id_book):
        query = """
        DELETE FROM `librarydb`.`description` 
        WHERE
            `librarydb`.`description`.id_description = %i;
        """ % id_book
        return query

    @staticmethod
    def add_row_in_table_author(author_name):
        if type(author_name) is not list:
            query = "INSERT INTO `librarydb`.`author`(`author_record`) VALUES ('%s');" % author_name
        else:
            query = "INSERT INTO `librarydb`.`author`(`author_record`) VALUES"
            query += " ('" + "'),('".join(author_name) + "');"
        return query

    @staticmethod
    def add_row_in_table_genre(genre_name):
        if type(genre_name) is not list:
            query = "INSERT INTO `librarydb`.`genre`(`genre_record`) VALUES ('%s');" % genre_name
        else:
            query = "INSERT INTO `librarydb`.`genre`(`genre_record`) VALUES"
            query += " ('" + "'),('".join (genre_name) + "');"
        return query

    @staticmethod
    def add_row_in_table_publisher(publisher_name):
        if type(publisher_name) is not list:
            query = "INSERT INTO `librarydb`.`publisher`(`publisher_record`) VALUES ('%s');" % publisher_name
        else:
            query = "INSERT INTO `librarydb`.`publisher`(`publisher_record`) VALUES"
            query += " ('" + "'),('".join (publisher_name) + "');"
        return query

    @staticmethod
    def add_row_in_table_bbk(bbk_index):
        if type(bbk_index) is not list:
            query = "INSERT INTO `librarydb`.`bbk`(`bbk_record`) VALUES ('%s');" % bbk_index
        else:
            query = "INSERT INTO `librarydb`.`bbk`(`bbk_record`) VALUES"
            query += " ('" + "'),('".join(bbk_index) + "');"
        return query

    @staticmethod
    def add_row_in_table_udc(udc_index):
        if type(udc_index) is not list:
            query = "INSERT INTO `librarydb`.`udc`(`udc_record`) VALUES ('%s');" % udc_index
        else:
            query = "INSERT INTO `librarydb`.`udc`(`udc_record`) VALUES"
            query += " ('" + "'),('".join(udc_index) + "');"
        return query

    @staticmethod
    def add_row_in_table_description(description):
        if type (description) is not list:
            query = "INSERT INTO `librarydb`.`description`(`description_record`) VALUES ('%s');" % description
        else:
            query = "INSERT INTO `librarydb`.`description`(`description_record`) VALUES"
            query += " ('" + "'),('".join(description) + "');"
        return query

    @staticmethod
    def add_row_in_table_file_tables(file_name, number_of_row):
        if type(file_name) is not list:
            query = "INSERT INTO `librarydb`.`filetables`(`file_name`, `number_of_row`)" \
                    " VALUES ('%s', %s);" % (str(file_name), str(number_of_row))
        return query

    @staticmethod
    def update_row_in_table_file_tables(file_name, number_of_row):
        if type(file_name) is not list:
            query = "UPDATE `librarydb`.`filetables` SET `number_of_row` = '%s' " \
                    "WHERE `file_name` = '%s';" % (str(number_of_row), str(file_name))
        return query

    @staticmethod
    def add_row_in_table_books(name_book, number_of_pages_book,
                               index_book_binding_type, release_date_book,
                               index_udc, index_bbk, index_publisher, isbn, description_record):
        if type(name_book) is not list:
            query = "INSERT INTO `librarydb`.`books`"\
                    "(`name_book`,`number_of_pages_book`,"\
                    "`index_book_binding_type`,`release_date_book`,"\
                    "`index_udc`,`index_bbk`, `index_publisher`,`isbn`, `description_record`)"\
                    " VALUES ('%s', %s, %s, %s, %s, %s, %s, '%s', '%s');"\
                    % (name_book, str(number_of_pages_book), str(index_book_binding_type),
                       str(release_date_book), str(index_udc), str(index_bbk), str(index_publisher),
                       isbn, description_record)
        else:
            query = "INSERT INTO `librarydb`.`books`" \
                    "(`name_book`,`number_of_pages_book`," \
                    "`index_book_binding_type`,`release_date_book`," \
                    "`index_udc`,`index_bbk`, `index_publisher`,`isbn`, `description_record`)" \
                    " VALUES"
            iterator = 0
            while iterator < len(name_book):
                query += "('" + name_book[iterator] + "'," + str(number_of_pages_book[iterator]) + "," +\
                         str(index_book_binding_type[iterator]) + "," + str(release_date_book[iterator]) + "," +\
                         str(index_udc[iterator]) + "," + str(index_bbk[iterator]) + "," +\
                         + str(index_publisher[iterator]) + ","\
                         + isbn[iterator] + "," + description_record[iterator] + "')"
                iterator += 1
                if iterator < len(name_book):
                    query += ","
                query += ";"
        return query

    @staticmethod
    def add_row_in_table_cache(id_books, name_book, author_group,
                               genre_group, index_bbk,index_udc,
                               isbn, publisher, number_of_pages_book,
                               binding_type, description_record, release_date_book):
        if type(name_book) is not list:
            query = "INSERT INTO `librarydb`.`cache`"\
                    "(`id_books`," \
                    "`name_book`," \
                    "`author_group`," \
                    "`genre_group`," \
                    "`index_bbk`," \
                    "`index_udc`," \
                    "`isbn`," \
                    "`publisher`," \
                    "`number_of_pages_book`," \
                    "`binding_type`," \
                    "`description_record`," \
                    "`release_date_book`)" \
                    " VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"\
                    % (id_books,
                       name_book,
                       author_group,
                       genre_group,
                       index_bbk,
                       index_udc,
                       isbn,
                       publisher,
                       number_of_pages_book,
                       binding_type,
                       description_record,
                       release_date_book)
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

    @staticmethod
    def get_author_null_id():
        query = """
            SELECT 
                librarydb.books.id_books
            FROM
                librarydb.books
            WHERE
            NOT librarydb.books.id_books IN (SELECT 
                `librarydb`.`books`.id_books
            FROM
                `librarydb`.`books`
                    JOIN
                `librarydb`.`genre_join_table` ON `librarydb`.`genre_join_table`.id_books = `librarydb`.`books`.id_books
                    JOIN
                `librarydb`.`genre` ON `librarydb`.`genre`.id_genre = `librarydb`.`genre_join_table`.id_genre
                    JOIN
                `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type = 
                `librarydb`.`books`.index_book_binding_type
                    JOIN
                `librarydb`.`publisher` ON `librarydb`.`publisher`.id_publisher = `librarydb`.`books`.index_publisher
                    JOIN
                `librarydb`.`udc` ON `librarydb`.`udc`.id_udc = `librarydb`.`books`.index_udc
                    JOIN
                `librarydb`.`bbk` ON `librarydb`.`bbk`.id_bbk = `librarydb`.`books`.index_bbk
            GROUP BY `librarydb`.`books`.id_books);
        """
        query1 = """        
        SELECT 
            `librarydb`.`books`.id_books
        FROM
            librarydb.books
        WHERE
            NOT `librarydb`.`books`.id_books IN (SELECT 
                    `librarydb`.`books`.id_books
                FROM
                    `librarydb`.`books`
                        JOIN
                    `librarydb`.`author_join_table` ON `librarydb`.`author_join_table`.id_books =
                     `librarydb`.`books`.id_books
                        JOIN
                    `librarydb`.`author` ON `librarydb`.`author`.id_author = `librarydb`.`author_join_table`.id_author
                        JOIN
                    `librarydb`.`genre_join_table` ON `librarydb`.`genre_join_table`.id_books =
                     `librarydb`.`books`.id_books
                        JOIN
                    `librarydb`.`genre` ON `librarydb`.`genre`.id_genre = `librarydb`.`genre_join_table`.id_genre
                        JOIN
                    `librarydb`.`book_binding_type` ON `librarydb`.`book_binding_type`.id_book_binding_type =
                     `librarydb`.`books`.index_book_binding_type
                        JOIN
                    `librarydb`.`publisher` ON `librarydb`.`publisher`.id_publisher =
                     `librarydb`.`books`.index_publisher
                        JOIN
                    `librarydb`.`udc` ON `librarydb`.`udc`.id_udc = `librarydb`.`books`.index_udc
                        JOIN
                    `librarydb`.`bbk` ON `librarydb`.`bbk`.id_bbk = `librarydb`.`books`.index_bbk
                GROUP BY `librarydb`.`books`.id_books);
        """

        return query1

    @staticmethod
    def get_genre_null_id():
        query = """
        SELECT librarydb.books.id_books
        FROM librarydb.books
        WHERE NOT librarydb.books.id_books IN (
        SELECT librarydb.genre_join_table.id_books FROM librarydb.genre_join_table);
        """
        return query


"""
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
    print(QueryFactory.show_all())
"""
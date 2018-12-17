"""!
@package Hierarchy
"""

class Hierarchy ():
    """!
        @brief Provides a hierarchical data model
        @brief Обеспечивает иерархическую модель данных
    """

    def get_book(self, level, index):
        item = 0
        return item

    def get_level_hierarchy(self, level_name):
        item = 0
        return item

    def get_level_book(self, level):
        item = 0
        return item

    def add_book(self, id_book, genre):
        level = None
        level = self.get_level_hierarchy(genre)
        if level is None:
            level = self.add_level_hierarchy(genre)
        add_item(id_book, level)
        item = 0
        return item


    def add_level_hierarchy(self, level_name):

        item = 0
        return item

    def remove_book(self, level, index):
        item = 0
        return item

    def remove_level(self, level):
        item = 0
        return item


import os
from database import DatabaseInspector
from queryfactory import QueryFactory

class fsdb(DatabaseInspector):

    list_file = []
    folder_patch = "tables"

    def __init__(self):
        if os.path.exists(self.folder_patch):
            self.list_file = os.listdir(self.folder_patch)
            for iterator in range(len(self.list_file)):
                self.list_file[iterator] = self.folder_patch+'/'+self.list_file[iterator]

    def add_list_file(self):
        for file in self.list_file:
            query = QueryFactory.add_row_in_table_file_tables(file, 0)
            #print(query)
            self.execute(query)

    def update(self, file_name, number_of_row):
        self.execute(QueryFactory.update_row_in_table_file_tables(file_name, number_of_row))

    def start_row_file(self, file_name):
        row_str = self.execute(QueryFactory.search_by_file_name(file_name))
        return int(row_str[0][0])

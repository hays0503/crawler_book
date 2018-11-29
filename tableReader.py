import openpyxl

"""
@package tableReader
"""

class tableInspector():
    """
        @brief Считывание и систиматизация данных из таблиц MS Excel
    """

    other_description = {}

    def __init__(self, patch_to_file, number_sheet=0):
        self.read_sheet(patch_to_file, number_sheet=0)

    def read_sheet(self, patch_to_file, number_sheet=0):
        """
            @brief Считывает страницу документа возвращая объект страница
        """
        wb = openpyxl.load_workbook(filename=patch_to_file,
                                    read_only=True)
        name_sheet = wb.sheetnames
        sheet = wb[name_sheet[number_sheet]]
        row_count = sheet.max_row
        for row in sheet.rows:
            turple = [row[1].value, row[4].value]
            other_description = str(turple[0]).rsplit(', ', 4)
            for i in range(len(other_description)):
                other_description[i] = other_description[i].capitalize()
            print(other_description)
        return other_description

    def name_book(self, row=0):
        return self.other_description[row]

    def autor_book(self, row=0):
        return self.other_description[row]

    def description_book(self, row=0):
        return self.other_description[row]

    def publisher_book(self, row=0):
        return self.other_description[row]

    def release_date_book(self, row=0):
        return self.other_description[row]

    def release_date_book(self, row=0):
        return self.other_description[row]


if __name__ == '__main__':
    table_Inspector = tableInspector(patch_to_file="prices_s2.xlsx")

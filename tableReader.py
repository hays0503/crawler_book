import openpyxl

"""
@package tableReader
"""

class tableInspector():
    """
        @brief Считывание и систиматизация данных из таблиц MS Excel
    """

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


if __name__ == '__main__':
    table_Inspector = tableInspector()
    table_Inspector.read_sheet(patch_to_file="prices_s2.xlsx")

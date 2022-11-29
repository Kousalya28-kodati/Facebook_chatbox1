import xlrd
from library.config import Config
# path=r"C:\Users\KOUSALYA\Downloads\Locators\Book1.xlsx"

class Reading_Excel:
    def read_locators(self):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
                    # worklook = xlrd.open_workbook(Config.TEST_PATH)
        worksheet = workbook.sheet_by_name(Config.DATA_PATH_TITLE)
                    # columns =worksheet.ncols
        rows=worksheet.get_rows()
        print(rows)
        header =next(rows)
        d={}
        for row in rows:
                d[row[0].value]=(row[1].value,row[2].value)
        return d
    # print(read_locators())






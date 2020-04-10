# -*- coding:utf-8 -*-
import xlrd
# data = xlrd.open_workbook('D:/www/zhaoliangji/app/dataconfig/interface.xlsx')
# tables = data.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(1, 1))
#
class OperationExcel:
    def __init__(self, file_name=None, sheets_id=None):
        if file_name:
            self.file_name = file_name
            self.sheets_id = sheets_id

        else:
            self.file_name = 'D:/www/zhaoliangji/app/dataconfig/interface.xlsx'
            self.sheets_id = 0
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheets_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, rowx, colx):
        return self.data.cell_value(rowx, colx)


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_data().nrows)
    print(opers.get_lines())
    print(opers.data.cell_value(1,1))

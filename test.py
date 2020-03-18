import os
from excel import Excel



# 打开文件
print('++++++++++++++++++++\n','debug','\n')
file_path = os.getcwd()+'/data.xlsx'


print("path:",file_path)
excel = Excel(file_path)    #创建实例化
print('all sheets')
list = []
list = excel.read_all_sheetnames(file_path)
print('sheet names：',list[0])


#sheet表名称
sname = list[0]
ord = excel.read_sheet_data(sname)
print(ord)
# 根据sheet索引或者名称获取sheet内容
#sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
# sheet1 = workbook.sheet_by_name('sheet2')
# sheet1的名称，行数，列数
# print(sheet1.name, sheet1.nrows, sheet1.ncols)
# # 获取整行和整列的值（数组）
# rows = sheet1.row_values(1) # 获取第三行内容
# cols = sheet1.col_values(0) # 获取第1列内容
# print(rows)
# print(cols)
# # 获取单元格内容
# print(sheet1.cell(1, 0).value.encode('utf-8'))
# print(sheet1.cell_value(1, 0).encode('utf-8'))
# print(sheet1.row(1)[0].value.encode('utf-8'))
# # 获取单元格内容的数据类型
# print(sheet1.cell(1, 0).ctype)
print('\n','end','\n++++++++++++++++++++')
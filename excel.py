
#用于副本操作
# 封装Excel类，用于操作excel文件，管理数据并CRUD
#Excel表需提前建好 表头也需提前在Excel表中写好
import xlrd
import xlwt
from xlutils.copy import copy
import os 
 
 
#TODO: 创建一个Excel表类
class Excel(object):
    def __init__(self, path):
        self.path = path #?绝对路径（带文件名）
        
        
 #TODO: 获取总共有多少个sheet
    def read_all_sheetnames(self, path):
        rd = xlrd.open_workbook(path)
        #sheets = rd.sheet_by_index(0)
        list = []
        list = rd.sheet_names()
        
               
        return list

#TODO: 读取Excel内全部数据 参数sname是sheet页名字 
    def read_sheet_data(self, sname): 
        workbook = xlrd.open_workbook(self.path)
        content = workbook.sheet_by_name(sname)#通过对象名称查询
        list = []
        #print(content)
        #获取总行数和列数

        merage = content.merged_cells #获取所有合并单元格坐标
        #格式的数据，(4, 5, 2, 4)的含义为：行从下标4开始，到下标5（不包含） 列从下标2开始，到下标4（不包含），为合并单元格，即C5 - 有勇有谋，单骑救主这个合并单元格
        #print("merage:",merage)

        rows = content.nrows
        cols = content.ncols

        #查找当前值是否有合并单元格
        for row_index in range(content.nrows):
            for col_index in range(content.ncols):
                for (rlow, rhigh, clow, chigh) in merage:
                    if (row_index >= rlow and row_index < rhigh):
                        if (col_index >= clow and col_index < chigh):
                            #print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                            cell_value = content.cell_value(rlow, clow)
                            list.append(cell_value)
                        else:
                            print("当前值不在合并单元格")
                            cell_value = content.cell_value(row_index,col_index)
                            list.append(cell_value)

        print(list)

        # ord_list = []
        # for rownum in range(content.nrows):
        #     ord_list.append(content.row_values(rownum))
        #     print(ord_list)
        #print(content)
        #返回的类型是一个list
        return list
 
 
#TODO:  写入单行Excel表
    # 参数obj指的是新添加的按表头顺序排列的list类型数据，
    # sname指的是sheet页名字
    def write_row_data(self, obj, sname):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        nrows=sheet.nrows
        new_wb = copy(wb)  # 将原有的Excel，拷贝一个新的副本
        new_sheet = new_wb.get_sheet(0) # 重新在新的Excel中获取
        for i in range(len(obj)):
            new_sheet.write(nrows,i,obj[i])
        new_wb.save(self.path)
        return '存入成功！'
 
 
#TODO: 修改单行数据
#obj传的是字典对象，{'ID':'***','要修改的某一表头':'修改的内容'}，sname指的是sheet名
    def write_cell_data(self, obj, sname):
        #3.1 获取当前指定 sheet
        #3.2 Copy
        #3.3 get_sheet(0)
        #3.4 循环查找当前 sheet 内容
        #3.4.1 对 obj的指定内容 要进行匹配 
        #3.4.1.1如果找到了 就修改 msg = ok
        #3.4.1.2没有找到 就得  msg = error
        #3.5 save
        #3.6 return msg
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        col_val=sheet.col_values(0)#第一列的值
        row_val=sheet.row_values(0)
        keys=list(obj.keys())
        set_col=0
        set_nrows=0
        # set_nrows=col_val.index(int(obj[keys[0]]))
        for j in range(len(col_val)):            
            if col_val[j]==obj[keys[0]]:
                set_nrows=j
        for i in range(len(row_val)):
            if row_val[i]==keys[1]:
                set_col=i
        if set_col==0 or set_nrows==0:
            msg=False
            return msg
        else:
            new_wb = copy(wb)
            new_sheet = new_wb.get_sheet(0)
            new_sheet.write(set_nrows,set_col,obj[keys[1]])
            new_wb.save(self.path)
            msg=True
            return msg
 
 
#TODO: 清空Excel表的内容，参数sname是sheet页名
    def delete_all_data(self,sname):
        red_all=self.read_all_data(sname)
        new_ord=[]
        new_ord.append(red_all[0])
        wbt = xlwt.Workbook()
            # 生成一个sheet页
        sheet = wbt.add_sheet(sname)
        for m in range(len(new_ord)):
            for n in range(len(new_ord[m])):
                sheet.write(m, n, new_ord[m][n])
        wbt.save(self.path)
 
 
#TODO: 删除某一行的数据，参数obj指的是某行，sname是sheet页名       
    def delete_row_data(self,obj,sname):
        wb = xlrd.open_workbook(self.path)
        sheet = wb.sheet_by_name(sname)
        col_val=sheet.col_values(0)#第一列的值
        del_nrows=0
        for j in range(len(col_val)):
            if col_val[j]==int(obj):
                del_nrows=j
        if del_nrows==0:
            msg=False
            return msg
        else:
            red_all=self.read_all_data(sname)
            a=red_all.pop(del_nrows)
            wbt = xlwt.Workbook()
            # 生成一个sheet页
            sheet = wbt.add_sheet(sname)
            for m in range(len(red_all)):
                for n in range(len(red_all[m])):
                    sheet.write(m, n, red_all[m][n])
            wbt.save(self.path)
            msg=True
            return msg
            
        
if __name__ == "__main__":
    pass
    #path __file__
    #动态获取路径 获取当前py文件 所在的目录
     #d = os.path.dirname(__file__)
    #获取当前py文件执行时候的父级目录
    #Excel(test.xls)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from test import Ui_demo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget, QTableView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon,QStandardItemModel,QStandardItem
from PyQt5.QtCore import QFileInfo
import os
import xlrd
import xlwt
from xlutils.copy import copy

from excel import Excel

class Ui_log_form(QtWidgets.QWidget):
    def setupUi(self, log_form):
        log_form.setObjectName("log_form")
        self.form = log_form
        log_form.resize(738, 696)

        self.log_text = QtWidgets.QTextEdit(log_form)
        self.log_text.setGeometry(QtCore.QRect(10, 490, 711, 201))
        self.log_text.setObjectName("log_text")

        self.user_label = QtWidgets.QLabel(log_form)
        self.user_label.setGeometry(QtCore.QRect(10, 470, 36, 12))
        self.user_label.setObjectName("user_label")

        self.file_path_text = QtWidgets.QTextEdit(log_form)
        self.file_path_text.setGeometry(QtCore.QRect(50, 40, 251, 31))
        self.file_path_text.setObjectName("file_path_text")

        self.file_path_button = QtWidgets.QPushButton(log_form)
        self.file_path_button.setGeometry(QtCore.QRect(320, 40, 61, 31))
        self.file_path_button.setObjectName("file_path_button")

        self.find_text = QtWidgets.QTextEdit(log_form)
        self.find_text.setGeometry(QtCore.QRect(50, 130, 251, 31))
        self.find_text.setObjectName("find_text")

        self.find_button = QtWidgets.QPushButton(log_form)
        self.find_button.setGeometry(QtCore.QRect(320, 130, 61, 31))
        self.find_button.setObjectName("find_button")

        self.return_button = QtWidgets.QPushButton(log_form)
        self.return_button.setGeometry(QtCore.QRect(610, 450, 61, 31))
        self.return_button.setObjectName("return_button")

        self.all_sheet_name_button = QtWidgets.QPushButton(log_form)
        self.all_sheet_name_button.setGeometry(QtCore.QRect(470, 450, 131, 31))
        self.all_sheet_name_button.setObjectName("all_sheet_name_button")

        self.label = QtWidgets.QLabel(log_form)
        self.label.setGeometry(QtCore.QRect(50, 110, 54, 12))
        self.label.setObjectName("label")

        self.tableWidget = QtWidgets.QTableWidget(log_form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 611, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1
                                     )
        self.label_2 = QtWidgets.QLabel(log_form)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 54, 12))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(log_form)
        QtCore.QMetaObject.connectSlotsByName(log_form)

    def retranslateUi(self, log_form):

        _translate = QtCore.QCoreApplication.translate
        log_form.setWindowTitle(_translate("log_form", "Dialog"))
        self.user_label.setText(_translate("log_form", "log"))
        self.file_path_button.setText(_translate("log_form", "浏览"))
        self.find_button.setText(_translate("log_form", "查找"))
        self.return_button.setText(_translate("log_form", "返回"))
        self.all_sheet_name_button.setText(_translate("log_form", "显示全部列表名称"))




        #案件事件
        self.return_button.clicked.connect(self.goto_login)
        self.find_button.clicked.connect(self.goto_find)
        self.all_sheet_name_button.clicked.connect(self.goto_allsheetname)
        self.file_path_button.clicked.connect(self.goto_filename)
    # 这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
    def goto_login(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_demo()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()


    def goto_filename(self):
       #file_path = QFileDialog.getExistingDirectory(self, "选取文件夹","/")
        global file_path
        file_path,type = QFileDialog.getOpenFileName(self,  "选取文件",  "./",  "All Files (*);;Text Files (*.txt)")
        print(file_path)
        print(type)
        self.file_path_text.append(file_path)
        return file_path


    def goto_allsheetname(self):
        print('++++++++++++++++++++\n', 'debug', '\n')


        str ="path:" + file_path + '\n'

        excel = Excel(file_path)  # 创建实例化
        print('all sheets')
        list = []
        list = excel.read_all_sheetnames(file_path)
        print('sheet names：', list)
        print('\n', 'end', '\n++++++++++++++++++++')
        str += "all sheet\n" + '； '.join(list)
        self.log_text.setPlainText(str)

    def goto_find(self):
        print('++++++++++++++++++++\n','debug','\n')
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
      #  j = 0  # 第几行（从0开始）
      #  i = 0  # 第几列（从0开始）
       # Value = "test"  # 内容
        #self.tableWidget.setItem(i, j, QTableWidgetItem(Value))  # 设置j行i列的内容为Value

       #excel.py处理单个sheet有内存溢出bug，暂时直接用
        str = self.find_text.toPlainText()#获取text的文本内容
        print(str)
        excel = Excel(file_path)
        excel.read_sheet_data(str)
        #print(list)
        #self.log_text.setPlainText(list)
        #self.log_text.setPlainText(content)
        #print(list)
        #self.log_text.append(self,list)
        #for i in range(list):
            #self.tableWidget.setItem(i,0,QTableWidgetItem(list[i]))
        #self.log_text.append(self,ord_list)
        # for i in range(len(list)):
        #     for j in range(len(list))：

       # self.tableWidget.setColumnWidth(j, 80)  # 设置j列的宽度
        #self.tableWidget.setRowHeight(i, 50)  # 设置i行的高度
       # self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
       # self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头



        print('\n','end','\n++++++++++++++++++++')

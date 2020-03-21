# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_form(object):
    def setupUi(self, log_form):
        log_form.setObjectName("log_form")
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
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
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
        self.label.setText(_translate("log_form", "关键字"))
        self.label_2.setText(_translate("log_form", "查询结果"))

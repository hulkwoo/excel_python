# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        self.login_button = QtWidgets.QPushButton(login)
        self.login_button.setGeometry(QtCore.QRect(110, 210, 75, 23))
        self.login_button.setObjectName("login_button")
        self.exit_button = QtWidgets.QPushButton(login)
        self.exit_button.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.exit_button.setObjectName("exit_button")
        self.user_label = QtWidgets.QLabel(login)
        self.user_label.setGeometry(QtCore.QRect(70, 90, 36, 12))
        self.user_label.setObjectName("user_label")
        self.key_label = QtWidgets.QLabel(login)
        self.key_label.setGeometry(QtCore.QRect(70, 130, 54, 12))
        self.key_label.setObjectName("key_label")
        self.user_textEdit = QtWidgets.QTextEdit(login)
        self.user_textEdit.setGeometry(QtCore.QRect(120, 80, 181, 31))
        self.user_textEdit.setObjectName("user_textEdit")
        self.key_textEdit = QtWidgets.QTextEdit(login)
        self.key_textEdit.setGeometry(QtCore.QRect(120, 120, 181, 31))
        self.key_textEdit.setObjectName("key_textEdit")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.login_button.setText(_translate("login", "登录"))
        self.exit_button.setText(_translate("login", "退出"))
        self.user_label.setText(_translate("login", "用户名"))
        self.key_label.setText(_translate("login", "密码"))
if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_login()
    ui.setupUi(widget)
   # widget.setWindowIcon(QIcon('web.png'))#增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())
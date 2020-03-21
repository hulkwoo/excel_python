# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import log_ui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_demo(object):
    def setupUi(self, demo):
        demo.setObjectName("demo")
        demo.resize(400, 300)
        self.form = demo
        self.return_button = QtWidgets.QPushButton(demo)
        self.return_button.setGeometry(QtCore.QRect(180, 150, 75, 23))
        self.return_button.setObjectName("return_button")

        self.retranslateUi(demo)
        QtCore.QMetaObject.connectSlotsByName(demo)

    def retranslateUi(self, demo):
        _translate = QtCore.QCoreApplication.translate
        demo.setWindowTitle(_translate("demo", "Dialog"))
        self.return_button.setText(_translate("demo", "start"))
        self.return_button.clicked.connect(self.goto_system)

    def goto_system(self):
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = log_ui.Ui_log_form()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_demo()  #实例化
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
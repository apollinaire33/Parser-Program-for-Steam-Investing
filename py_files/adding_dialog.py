from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import xlwt
import xlrd
import xlsxwriter
import openpyxl 
import webbrowser
import datetime
import os


class Ui_DialogWindow(object):

    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(424, 446)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        DialogWindow.setFont(font)
        self.label = QtWidgets.QLabel(DialogWindow)
        self.label.setGeometry(QtCore.QRect(170, 40, 92, 24))
        font = QtGui.QFont()
        font.setFamily("Narkisim")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.EnterURLLine = QtWidgets.QLineEdit(DialogWindow)
        self.EnterURLLine.setGeometry(QtCore.QRect(60, 130, 301, 31))
        self.EnterURLLine.setObjectName("EnterURLLine")
        self.EnterAmountLine = QtWidgets.QLineEdit(DialogWindow)
        self.EnterAmountLine.setGeometry(QtCore.QRect(60, 200, 301, 31))
        self.EnterAmountLine.setObjectName("EnterAmountLine")
        self.EnterPriceLine = QtWidgets.QLineEdit(DialogWindow)
        self.EnterPriceLine.setGeometry(QtCore.QRect(60, 270, 301, 31))
        self.EnterPriceLine.setObjectName("EnterPriceLine")
        self.label_2 = QtWidgets.QLabel(DialogWindow)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogWindow)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogWindow)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.AddButton = QtWidgets.QPushButton(DialogWindow)
        self.AddButton.setGeometry(QtCore.QRect(120, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AddButton.setFont(font)
        self.AddButton.setObjectName("AddButton")
        self.CancelButton = QtWidgets.QPushButton(DialogWindow)
        self.CancelButton.setGeometry(QtCore.QRect(220, 360, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CancelButton.setFont(font)
        self.CancelButton.setObjectName("CancelButton")

        DialogWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'logo.png')))
        DialogWindow.setWindowModality(Qt.ApplicationModal)
        
        

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, DialogWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogWindow.setWindowTitle(_translate("DialogWindow", "Adding New Item"))
        self.label.setText(_translate("DialogWindow", "New Item"))
        self.label_2.setText(_translate("DialogWindow", "Enter URL:"))
        self.label_3.setText(_translate("DialogWindow", "Enter Amount:"))
        self.label_4.setText(_translate("DialogWindow", "Enter Price:"))
        self.AddButton.setText(_translate("DialogWindow", "Add"))
        self.CancelButton.setText(_translate("DialogWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogWindow = QtWidgets.QWidget()
    ui = Ui_DialogWindow()
    ui.setupUi(DialogWindow)
    DialogWindow.show()
    sys.exit(app.exec_())

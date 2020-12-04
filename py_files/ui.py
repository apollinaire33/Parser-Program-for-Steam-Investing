from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 626)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(213, 213, 213);\n"
"    \n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 631, 21))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setEnabled(True)
        self.Name.setGeometry(QtCore.QRect(20, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.Name.setFont(font)
        self.Name.setLineWidth(100)
        self.Name.setTextFormat(QtCore.Qt.AutoText)
        self.Name.setObjectName("Name")
        self.Price = QtWidgets.QLabel(Form)
        self.Price.setEnabled(True)
        self.Price.setGeometry(QtCore.QRect(20, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.Price.setFont(font)
        self.Price.setLineWidth(100)
        self.Price.setTextFormat(QtCore.Qt.AutoText)
        self.Price.setObjectName("Price")
        self.Amount = QtWidgets.QLabel(Form)
        self.Amount.setEnabled(True)
        self.Amount.setGeometry(QtCore.QRect(20, 120, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.Amount.setFont(font)
        self.Amount.setLineWidth(100)
        self.Amount.setTextFormat(QtCore.Qt.AutoText)
        self.Amount.setObjectName("Amount")
        self.NameOutput = QtWidgets.QLabel(Form)
        self.NameOutput.setEnabled(True)
        self.NameOutput.setGeometry(QtCore.QRect(170, 60, 611, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.NameOutput.setFont(font)
        self.NameOutput.setStyleSheet("font: 14pt \"MS UI Gothic\";\n"
"font-weight:600;")
        self.NameOutput.setLineWidth(100)
        self.NameOutput.setTextFormat(QtCore.Qt.AutoText)
        self.NameOutput.setObjectName("NameOutput")
        self.AmountOutput = QtWidgets.QLabel(Form)
        self.AmountOutput.setEnabled(True)
        self.AmountOutput.setGeometry(QtCore.QRect(170, 120, 611, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.AmountOutput.setFont(font)
        self.AmountOutput.setStyleSheet("font: 14pt \"MS UI Gothic\";\n"
"font-weight:600;")
        self.AmountOutput.setLineWidth(100)
        self.AmountOutput.setTextFormat(QtCore.Qt.AutoText)
        self.AmountOutput.setObjectName("AmountOutput")
        self.PriceOutput = QtWidgets.QLabel(Form)
        self.PriceOutput.setEnabled(True)
        self.PriceOutput.setGeometry(QtCore.QRect(170, 90, 611, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PriceOutput.setFont(font)
        self.PriceOutput.setStyleSheet("font: 14pt \"MS UI Gothic\";\n"
"font-weight:600;")
        self.PriceOutput.setLineWidth(100)
        self.PriceOutput.setTextFormat(QtCore.Qt.AutoText)
        self.PriceOutput.setObjectName("PriceOutput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Parsing"))
        self.lineEdit.setPlaceholderText(_translate("Form", "enter URL"))
        self.Name.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Product Name: </span></p></body></html>"))
        self.Price.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Price: </span></p></body></html>"))
        self.Amount.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Amount: </span></p></body></html>"))
        self.NameOutput.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.AmountOutput.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.PriceOutput.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))



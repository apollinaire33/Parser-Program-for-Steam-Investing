from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import xlwt
import xlrd
import xlsxwriter
import openpyxl 
from adding_dialog import Ui_DialogWindow
import webbrowser
import datetime
import os 
import requests
import json 
from bs4 import BeautifulSoup as BS
import re
import webbrowser
import time
import sys


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


p_amount_sum = 0
p_paid_sum = 0
p_price_sum = 0
p_invested_sum = 0
p_nocomm_sum = 0
p_earned_sum = 0
p_profit_sum = 0
p_profit1_sum = 0

Adding = False
Loading = False
qwe = 0
class Ui_MainWindow(object):
    def OpenAddDialog(self):
        global DialogWindow, Adding
        DialogWindow = QtWidgets.QWidget()
        ui = Ui_DialogWindow()
        ui.setupUi(DialogWindow)
        DialogWindow.show()
        
        def EnterData():
            global p_amount_sum, p_paid_sum, p_price_sum, p_invested_sum, p_nocomm_sum, p_earned_sum, p_profit_sum, p_profit1_sum
            global p_amount, p_paid, p_price, p_invested, p_nocomm, p_earned, p_profit, p_profit1, Adding
            try:
                Adding = True
                url = ui.EnterURLLine.text()
                p_amount = ui.EnterAmountLine.text()
                p_paid_q = ui.EnterPriceLine.text()
                p_paid = p_paid_q.replace(',','.')

                response = requests.get(url)

                result = re.findall(r'Market_LoadOrderSpread\(\s*(\d+)\s*\)', str(response.content))
                start = '"market_hash_name":"'
                end = '"'
                result_name1 = re.search('{}.*?{}'.format(*map(re.escape, [start, end])), str(response.content), re.M).group()
                result_name = result_name1[20:-1]

                json_url = 'https://steamcommunity.com/market/itemordershistogram?country=BY&language=russian&currency=1&item_nameid=' + str(result[0]) + '&two_factor=0'
                json_response = requests.get(json_url)

                json_data = json_response.json()
                json_sorted = json_data["sell_order_graph"]

                p_name = str(result_name)
                p_price = json_sorted[0][0]
                p_invested = float(p_paid) * float(p_amount)
                p_nocomm = float(p_price) * 8693 / 10000
                p_earned = float(p_amount) * float(p_nocomm)
                p_profit = float(p_earned) - float(p_invested)
                if p_profit < 0:
                    p_profit1 = (float(p_invested) * -100 / float(p_earned)) + 100
                else:
                    p_profit1 = (float(p_earned) * 100 / float(p_invested)) - 100

                p_amount_sum = p_amount_sum + int(p_amount)
                p_paid_sum = p_paid_sum + float(p_paid)
                p_price_sum = p_price_sum + p_price
                p_invested_sum = p_invested_sum + p_invested
                p_nocomm_sum = p_nocomm_sum + p_nocomm
                p_earned_sum = p_earned_sum + p_earned
                p_profit_sum = p_profit_sum + p_profit
                p_profit1_sum = p_profit1_sum + p_profit1

                logged_in = False
                if logged_in == True:
                    data = [str( p_name ), str( url ), str( p_amount ), str( round(float(p_paid), 2) ) + ' ₽', str( round(p_invested, 2) ) + ' ₽', str( round(p_price, 2) ) + ' ₽', str( round(p_nocomm, 2) ) + ' ₽', str( round(p_earned, 2) ) + ' ₽', str( round(p_profit, 2) ) + ' ₽', str( str(round(p_profit1, 2)) + ' %' )]
                else:
                    data = [str( p_name ), str( url ), str( p_amount ), str( round(float(p_paid), 2) ), str( round(p_invested, 2) ), str( round(p_price, 2) ), str( round(p_nocomm, 2) ), str( round(p_earned, 2) ), str( round(p_profit, 2) ), str( str(round(p_profit1, 2)) )]
                
                def AddNewRow():
                    row = 1
                    self.tableWidget.insertRow(row)
                    x = -1
                    column = -1
                    while x != 9:
                        column += 1
                        x += 1
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(data[x]))
                    
                    row = row + 1

                    amount_upd = 0
                    paid_upd = 0
                    invest_upd = 0
                    price_upd = 0
                    nocomm_upd = 0
                    earned_upd = 0
                    profit_upd = 0
                    profit1_upd = 0
                        
                    for i in range(1, 100):
                        summary = 'Summary'
                        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(summary))

                        amount_list = self.tableWidget.item(i, 2)
                        amount_upd += int(amount_list.text())
                        amount_str = QTableWidgetItem(str(amount_upd), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 2, amount_str)

                        paid_list = self.tableWidget.item(i, 3)
                        paid_upd += float(paid_list.text())
                        paid_str = QTableWidgetItem(str(round(paid_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 3, paid_str)

                        invest_list = self.tableWidget.item(i, 4)
                        invest_upd += float(invest_list.text())
                        invest_str = QTableWidgetItem(str(round(invest_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 4, invest_str)

                        price_list = self.tableWidget.item(i, 5)
                        price_upd += float(price_list.text())
                        price_str = QTableWidgetItem(str(round(price_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 5, price_str)

                        nocomm_list = self.tableWidget.item(i, 6)
                        nocomm_upd += float(nocomm_list.text())
                        nocomm_str = QTableWidgetItem(str(round(nocomm_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 6, nocomm_str)

                        earned_list = self.tableWidget.item(i, 7)
                        earned_upd += float(earned_list.text())
                        earned_str = QTableWidgetItem(str(round(earned_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 7, earned_str)

                        profit_list = self.tableWidget.item(i, 8)
                        profit_upd += float(profit_list.text())
                        profit_str = QTableWidgetItem(str(round(profit_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 8, profit_str)

                        profit1_list = self.tableWidget.item(i, 9)
                        profit1_upd += float(profit1_list.text())
                        profit1_str = QTableWidgetItem(str(round(profit1_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 9, profit1_str)
            
                AddNewRow()

            except:
                pass

            DialogWindow.close()
            Adding = False

        def CancelDialog(self):
            DialogWindow.close()

        ui.AddButton.clicked.connect( EnterData )
        ui.CancelButton.clicked.connect( CancelDialog )
        

        

    def Update(self, item):
        global qwe
        p_amount_sum = self.tableWidget.item(0, 2)
        if (item.column() == 2 or item.column() == 3):
            upd_amount = self.tableWidget.item(item.row(), 2)
            upd_paid = self.tableWidget.item(item.row(), 3)
            url = self.tableWidget.item(item.row(), 1)
            if upd_amount and upd_paid and Adding == False:
                try: 
                    response = requests.get(url.text())
                    result = re.findall(r'Market_LoadOrderSpread\(\s*(\d+)\s*\)', str(response.content))

                    json_url = 'https://steamcommunity.com/market/itemordershistogram?country=BY&language=russian&currency=1&item_nameid=' + str(result[0]) + '&two_factor=0'
                    json_response = requests.get(json_url)

                    json_data = json_response.json()
                    json_sorted = json_data["sell_order_graph"]

                    p_price = json_sorted[0][0]

                    if Loading == True:
                        time.sleep(15)

                    inv_resp = float(upd_amount.data(Qt.DisplayRole)) * float(upd_paid.data(Qt.DisplayRole))
                    nocomm_rest = float(p_price) * 8693 / 10000
                    rest_earned = float(upd_amount.data(Qt.DisplayRole)) * float(nocomm_rest)
                    rest_profit = float(rest_earned) - float(inv_resp)
                    if rest_profit < 0:
                        rest_profit1 = (float(inv_resp) * -100 / float(rest_earned)) + 100
                    else:
                        rest_profit1 = (float(rest_earned) * 100 / float(inv_resp)) - 100

                    upd_invested = QTableWidgetItem(str(inv_resp), QTableWidgetItem.Type)
                    upd_price = QTableWidgetItem(str(p_price), QTableWidgetItem.Type)
                    upd_nocomm = QTableWidgetItem(str( round(nocomm_rest, 2) ), QTableWidgetItem.Type)
                    upd_earned = QTableWidgetItem(str( round(rest_earned, 2) ), QTableWidgetItem.Type)
                    upd_profit = QTableWidgetItem(str( round(rest_profit, 2) ), QTableWidgetItem.Type)
                    upd_profit1 = QTableWidgetItem(str( round(rest_profit1, 2) ), QTableWidgetItem.Type)
                    
                    self.tableWidget.setItem(item.row(), 4, upd_invested)
                    self.tableWidget.setItem(item.row(), 5, upd_price)
                    self.tableWidget.setItem(item.row(), 6, upd_nocomm)
                    self.tableWidget.setItem(item.row(), 7, upd_earned)
                    self.tableWidget.setItem(item.row(), 8, upd_profit)
                    self.tableWidget.setItem(item.row(), 9, upd_profit1)
                    
                    amount_upd = 0
                    paid_upd = 0
                    invest_upd = 0
                    price_upd = 0
                    nocomm_upd = 0
                    earned_upd = 0
                    profit_upd = 0
                    profit1_upd = 0

                    for i in range(1, 100):
                        summary = 'Summary'
                        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(summary))

                        amount_list = self.tableWidget.item(i, 2)
                        amount_upd += int(amount_list.text())
                        amount_str = QTableWidgetItem(str(amount_upd), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 2, amount_str)

                        paid_list = self.tableWidget.item(i, 3)
                        paid_upd += float(paid_list.text())
                        paid_str = QTableWidgetItem(str(round(paid_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 3, paid_str)

                        invest_list = self.tableWidget.item(i, 4)
                        invest_upd += float(invest_list.text())
                        invest_str = QTableWidgetItem(str(round(invest_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 4, invest_str)

                        price_list = self.tableWidget.item(i, 5)
                        price_upd += float(price_list.text())
                        price_str = QTableWidgetItem(str(round(price_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 5, price_str)

                        nocomm_list = self.tableWidget.item(i, 6)
                        nocomm_upd += float(nocomm_list.text())
                        nocomm_str = QTableWidgetItem(str(round(nocomm_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 6, nocomm_str)

                        earned_list = self.tableWidget.item(i, 7)
                        earned_upd += float(earned_list.text())
                        earned_str = QTableWidgetItem(str(round(earned_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 7, earned_str)

                        profit_list = self.tableWidget.item(i, 8)
                        profit_upd += float(profit_list.text())
                        profit_str = QTableWidgetItem(str(round(profit_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 8, profit_str)

                        profit1_list = self.tableWidget.item(i, 9)
                        profit1_upd += float(profit1_list.text())
                        profit1_str = QTableWidgetItem(str(round(profit1_upd, 2)), QTableWidgetItem.Type)
                        self.tableWidget.setItem(0, 9, profit1_str)
                    
                except:
                    pass 

    def saveFile(self):
        try:
            filename = QFileDialog.getSaveFileName(directory=str(datetime.datetime.now().date()), filter="XLSX Files (*.xlsx);;All Files (*)")    
            wbk = openpyxl.Workbook()
            sheet = wbk.active 
            self.add2(sheet)
            wbk.save(str(filename[0]))          
        except:
            pass 
        
    def add2(self, sheet):
        for currentColumn in range(self.tableWidget.columnCount()):
            for currentRow in range(self.tableWidget.rowCount()):
                try:
                    teext = str(self.tableWidget.item(currentRow, currentColumn).text())
                    sheet.cell(row=( currentRow + 1 ), column= ( currentColumn + 1 ) ).value = teext   
                except AttributeError:
                    pass

    def loadData(self):
        global Loading
        Loading = True
        filename = QFileDialog.getOpenFileName()

        book = xlrd.open_workbook(str(filename[0]))
        sheet = book.sheets()[0] 
        data = [[sheet.cell_value(r,c) for c in range(0, 4)] for r in range(sheet.nrows)]

        self.tableWidget.setRowCount(0)

        for row, columnvalues in enumerate(data):
            self.tableWidget.insertRow(row)
            for column, value in enumerate(columnvalues):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))     
        Loading = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1170, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(137)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(1)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(8, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(9, QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().resizeSection(0, 350)
        self.tableWidget.horizontalHeader().resizeSection(1, 1)
        self.tableWidget.horizontalHeader().resizeSection(2, 75)
        self.tableWidget.horizontalHeader().resizeSection(3, 60)
        self.tableWidget.horizontalHeader().resizeSection(4, 85)
        self.tableWidget.horizontalHeader().resizeSection(5, 60)
        self.tableWidget.horizontalHeader().resizeSection(6, 95)
        self.tableWidget.horizontalHeader().resizeSection(7, 95)
        self.tableWidget.horizontalHeader().resizeSection(8, 95)
        self.tableWidget.horizontalHeader().resizeSection(9, 95)

        

        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        self.menuasdasdd = QtWidgets.QMenu(self.menubar)
        self.menuasdasdd.setObjectName("menuasdasdd")
        self.menuAdd_new_Item = QtWidgets.QMenu(self.menubar)
        self.menuAdd_new_Item.setObjectName("menuAdd_new_Item")
        self.menuLog_In = QtWidgets.QMenu(self.menubar)
        self.menuLog_In.setObjectName("menuLog_In")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionasdasdads = QtWidgets.QAction(MainWindow)
        self.actionasdasdads.setObjectName("actionasdasdads")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAdd_new = QtWidgets.QAction(MainWindow)
        self.actionAdd_new.setObjectName("actionAdd_new")
        self.menuasdasdd.addAction(self.actionasdasdads)
        self.menuasdasdd.addAction(self.actionLoad)
        self.menuAdd_new_Item.addAction(self.actionAdd_new)
        self.menubar.addAction(self.menuasdasdd.menuAction())
        self.menubar.addAction(self.menuAdd_new_Item.menuAction())
        self.menubar.addAction(self.menuLog_In.menuAction())

        self.tableWidget.itemChanged.connect( self.Update )

        delegate = AlignDelegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)

        self.actionAdd_new.triggered.connect( self.OpenAddDialog )

        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'logo.png')))
        self.actionLoad.triggered.connect( self.loadData )
        self.actionasdasdads.triggered.connect( self.saveFile )

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Invest Helper"))
        self.menuasdasdd.setTitle(_translate("MainWindow", "File"))
        self.menuAdd_new_Item.setTitle(_translate("MainWindow", "Items"))
        self.menuLog_In.setTitle(_translate("MainWindow", "Log In"))
        self.actionasdasdads.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAdd_new.setText(_translate("MainWindow", "Add new"))

        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Paid"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Invested"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FMainWindoworm", "Price"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "No Comm"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Earned"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Profit"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Profit %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Form
import requests
import json 
from bs4 import BeautifulSoup as BS
import re

# create application
app = QtWidgets.QApplication(sys.argv)

# create form and init UI
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# hook logic

def parser():

    url = ui.lineEdit.text()

    response = requests.get(url)

    result = re.findall(r'Market_LoadOrderSpread\(\s*(\d+)\s*\)', str(response.content))
    result_name = re.findall(r'market_hash_name":"(\D+)","commodity', str(response.content))

    json_url = 'https://steamcommunity.com/market/itemordershistogram?country=BY&language=russian&currency=1&item_nameid=' + str(result[0]) + '&two_factor=0'
    json_response = requests.get(json_url)

    json_data = json_response.json()
    json_sorted = json_data["sell_order_graph"]

    p_name = str(result_name[0])
    p_price = '$' + str(float(json_sorted[0][0]))
    p_amount = str(json_sorted[0][1])

    ui.NameOutput.setText(p_name)
    ui.PriceOutput.setText(p_price)
    ui.AmountOutput.setText(p_amount)

ui.pushButton.clicked.connect( parser )

# run main loop     
sys.exit(app.exec_())
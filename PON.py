from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from pyparsing import line_end

app = QApplication([])
win = QWidget()
win.resize(500,500)
win.setWindowTitle("Тест ГітХаб")
tittle= QLabel("Тестовий додаток для ГітХаб")

line_h= QHBoxLayout()
line_h.addWidget(tittle)
win.setLayout(line_h)
win.show()
app.exec_()

#Basic PyQt5 app structure

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(150, 150, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h3>My First PyQt5 GUI!</h3>', parent=window)
helloMsg.move(60, 15)


window.show()

sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import *
from wnd import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = WindowDefault()
    sys.exit(app.exec())
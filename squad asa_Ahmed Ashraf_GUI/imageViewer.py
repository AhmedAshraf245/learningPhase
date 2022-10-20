from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("image.ui", self)

        self.viewButton = self.findChild(QPushButton, "pushButton")
        self.deleteButton = self.findChild(QPushButton, "pushButton_2")
        self.viewRegion = self.findChild(QLabel, "label")

        self.viewButton.clicked.connect(self.clicked)
        self.deleteButton.clicked.connect(self.removed)

        self.show()

    def clicked(self):
        imgFrame = QFileDialog.getOpenFileName(self, "Open File", "c:\\Pictures", "All Files (*)")

        if imgFrame:
            self.pixmap = QPixmap(imgFrame[0])
            self.viewRegion.setPixmap(self.pixmap)

    def removed(self):
        self.viewRegion.clear()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

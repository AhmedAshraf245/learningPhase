from PyQt5 import QtCore, QtGui, QtWidgets

flag = 0
# This variable is used to check if the buton pressed after a calculate is a number and if so it will clear the screen otherwise it will keep the screen contents and continue in the operation

class Ui_Calculator(object):


    def calc(self):
        global flag
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("Error!")
        flag = 1

    def pressed(self, text):
        global flag
        if text == "C":
            self.outputLabel.setText("0")
        elif flag and (
                text == "0" or text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9"):
            self.outputLabel.setText(text)
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(self.outputLabel.text() + text)
        flag = 0

    def remove(self):
        screenCurrent = self.outputLabel.text()
        screenCurrent = screenCurrent[:-1]
        self.outputLabel.setText(screenCurrent)

    def clear(self):
        self.outputLabel.setText("0")

    def percent(self):
        self.outputLabel.setText(self.outputLabel.text() + "*0.01")

    def brackets(self):
        self.outputLabel.setText("(" + self.outputLabel.text() + ")")

    def decimel(self):
        chars = ["+", "-", "/", "%"]
        screen = self.outputLabel.text()
        if "." not in screen:
            self.outputLabel.setText(screen + ".")
        else:
            for i in chars:
                if i in screen and screen[-1] != ".":
                    self.outputLabel.setText(screen + ".")

    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(362, 585)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setIndent(-1)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.percent())
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear())
        self.clearButton.setGeometry(QtCore.QRect(100, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove())
        self.backButton.setGeometry(QtCore.QRect(190, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("/"))
        self.divideButton.setGeometry(QtCore.QRect(280, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.button9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("9"))
        self.button9.setGeometry(QtCore.QRect(190, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.button8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("8"))
        self.button8.setGeometry(QtCore.QRect(100, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(280, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.button7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("7"))
        self.button7.setGeometry(QtCore.QRect(10, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.button6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("6"))
        self.button6.setGeometry(QtCore.QRect(190, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.button5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("5"))
        self.button5.setGeometry(QtCore.QRect(100, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.subButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("-"))
        self.subButton.setGeometry(QtCore.QRect(280, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.subButton.setFont(font)
        self.subButton.setObjectName("subButton")
        self.button4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("4"))
        self.button4.setGeometry(QtCore.QRect(10, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("3"))
        self.button3.setGeometry(QtCore.QRect(190, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("2"))
        self.button2.setGeometry(QtCore.QRect(100, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("+"))
        self.addButton.setGeometry(QtCore.QRect(280, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.button1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("1"))
        self.button1.setGeometry(QtCore.QRect(10, 380, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.equButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.calc())
        self.equButton.setGeometry(QtCore.QRect(280, 470, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.equButton.setFont(font)
        self.equButton.setObjectName("equButton")
        self.button0 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed("0"))
        self.button0.setGeometry(QtCore.QRect(100, 470, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.bracketButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.brackets())
        self.bracketButton.setGeometry(QtCore.QRect(10, 470, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.bracketButton.setFont(font)
        self.bracketButton.setObjectName("bracketButton")
        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.decimel())
        self.dotButton.setGeometry(QtCore.QRect(190, 470, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.outputLabel.setText(_translate("Calculator", "0"))
        self.percentButton.setText(_translate("Calculator", "%"))
        self.clearButton.setText(_translate("Calculator", "C"))
        self.backButton.setText(_translate("Calculator", "<<"))
        self.divideButton.setText(_translate("Calculator", "/"))
        self.button9.setText(_translate("Calculator", "9"))
        self.button8.setText(_translate("Calculator", "8"))
        self.multiplyButton.setText(_translate("Calculator", "X"))
        self.button7.setText(_translate("Calculator", "7"))
        self.button6.setText(_translate("Calculator", "6"))
        self.button5.setText(_translate("Calculator", "5"))
        self.subButton.setText(_translate("Calculator", "-"))
        self.button4.setText(_translate("Calculator", "4"))
        self.button3.setText(_translate("Calculator", "3"))
        self.button2.setText(_translate("Calculator", "2"))
        self.addButton.setText(_translate("Calculator", "+"))
        self.button1.setText(_translate("Calculator", "1"))
        self.equButton.setText(_translate("Calculator", "="))
        self.button0.setText(_translate("Calculator", "0"))
        self.bracketButton.setText(_translate("Calculator", "( )"))
        self.dotButton.setText(_translate("Calculator", "."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

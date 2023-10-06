from PyQt5 import QtCore, QtGui, QtWidgets

from gestione import Gestore

gestore = Gestore()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 558)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_R5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_R5.setGeometry(QtCore.QRect(80, 200, 271, 221))
        self.frame_R5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_R5.setStyleSheet("QFrame {\n"
"    border: 5px solid black; /* Imposta il colore del bordo su rosso (cambia \"red\" con il colore desiderato) */\n"
"    background-image: url("+gestore.returnPth()+"DATACOM/QtResources/R5imm.PNG);\n"
"border-radius: 20px;\n"
"}")
        self.frame_R5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_R5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_R5.setObjectName("frame_R5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 60, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_R6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_R6.setGeometry(QtCore.QRect(450, 200, 271, 221))
        self.frame_R6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_R6.setStyleSheet("QFrame {\n"
"    border: 5px solid black; /* Imposta il colore del bordo su rosso (cambia \"red\" con il colore desiderato) */\n"
"    background-image: url("+gestore.returnPth()+"DATACOM/QtResources/R6imm.PNG);\n"
"border-radius: 20px;\n"
"}")
        self.frame_R6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_R6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_R6.setObjectName("frame_R6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.frame_R5.mousePressEvent = lambda event: self.openmanagement(event, "R5")
        self.frame_R6.mousePressEvent = lambda event: self.openmanagement(event, "R6")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CHOICE OPTIMIZE"))

    def openmanagement(self, event, sysname):
        from Manage import Ui_Manage
        self.management = QtWidgets.QFrame()
        self.ui = Ui_Manage()
        self.ui.setupUi(self.management, sysname)
        self.management.show()
        self.start.close()

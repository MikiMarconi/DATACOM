import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from ConnectionSSH import Connection
from gestione import Gestore
import time


gestore = Gestore()


class Ui_Manage(object):
    def setupUi(self, Form, sysname):
        Form.setObjectName("Form")
        Form.resize(1066, 531)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setWindowOpacity(1.0)
        self.form2 = Form
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setGeometry(QtCore.QRect(20, 280, 1031, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("# Nascondi il bordo della QTableWidget\n"
"QTableWidget {\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(0)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 1051, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 480, 1051, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 280, 21, 201))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1030, 270, 21, 211))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(660, 10, 221, 231))
        self.frame.setStyleSheet("background-image: url("+gestore.returnPth()+"DATACOM/QtResources/manageport.PNG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 450, 61, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gestore.returnPth()+"DATACOM/QtResources/iconaindietro.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.viewintbtn = QtWidgets.QPushButton(Form)
        self.viewintbtn.setGeometry(QtCore.QRect(740, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.viewintbtn.setFont(font)
        self.viewintbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewintbtn.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(gestore.returnPth()+"DATACOM/QtResources/iconaregistrazione.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewintbtn.setIcon(icon1)
        self.viewintbtn.setIconSize(QtCore.QSize(45, 45))
        self.viewintbtn.setObjectName("viewintbtn")
        self.populateTable(self.getInterfaceInfo(sysname), sysname)


        self.viewintbtn.clicked.connect(self.openViewInterface)
        self.pushButton_2.clicked.connect(self.openRouterChoice)
        self.viewintbtn.clicked.connect(self.openViewInterface)


        self.retranslateUi(Form, sysname)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, sysname):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tableWidget.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Interface Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "PHY"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Protocol"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "OutUti"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "InUti"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "InErrors"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "OutErrors"))
        self.label.setText(f"{sysname} MANAGEMENT")
        self.viewintbtn.setText(_translate("Form", " View Interfaces"))

    def openViewInterface(self, event):
        from ViewInt import Ui_ViewInt
        self.viewint = QtWidgets.QFrame()
        self.ui = Ui_ViewInt()
        self.ui.setupUi(self.viewint)
        self.viewint.show()


    def openRouterChoice(self, event):
        from StartUi import Ui_MainWindow
        self.back = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.back)
        self.back.show()
        self.form2.close()



    def getInterfaceInfo(self, sysname):

        port = "22"  # Sostituisci con la porta corretta
        username = "admin"  # Sostituisci con l'username corretto
        password = "huawei123"  # Sostituisci con la password corretta
        device_type = "huawei_vrp"  # Sostituisci con il tipo di dispositivo corretto

        if sysname == "R6":
            host = "10.100.0.10"  # Sostituisci con l'indirizzo IP corretto

        else:
            host = "10.100.0.9"  # Sostituisci con l'indirizzo IP corretto

        connection_instance = Connection()
        interfaces = connection_instance.splitOutput(host, port, username, password, device_type)
        return interfaces

    def populateTable(self, interfaces, sysname):
        def updateTable():
            while True:
                new_interfaces = self.getInterfaceInfo(sysname)
                # Rimuovi tutte le righe esistenti dalla tabella
                self.tableWidget.setRowCount(0)

                for row, interfaccia in enumerate(new_interfaces):
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(interfaccia.interface))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(interfaccia.phy))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(interfaccia.protocol))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(interfaccia.InUti))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(interfaccia.OutUti))
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(interfaccia.inErrors))
                    self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(interfaccia.outErrors))

                    self.tableWidget.setColumnWidth(0, 200)

                # Attendi 60 secondi prima di aggiornare nuovamente
                time.sleep(5)

        # Crea e avvia il thread di aggiornamento della tabella
        update_thread = threading.Thread(target=updateTable)
        update_thread.daemon = True  # Imposta il thread come daemon per terminarlo quando si chiude l'applicazione
        update_thread.start()


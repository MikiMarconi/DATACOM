import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

from ConnectionSSH import Connection

class Ui_Form(object):
    def setupUi(self, Form, sysname):

        Form.setObjectName("Form")
        Form.resize(1066, 531)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 941, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 21, 321))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(1040, 10, 21, 331))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 1051, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 340, 931, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setEnabled(False)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 60, 1031, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setStyleSheet("# Nascondi il bordo della QTableWidget\n"
"QTableWidget {\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setAutoScrollMargin(0)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
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
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(49)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 1051, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.label.raise_()
        self.tableWidget_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.timer = QTimer(Form)
        self.timer.timeout.connect(lambda: self.showTracert(sysname))  # Sostituisci "R5" con il valore desiderato per sysname
        self.timer.start(5000)
        self.populateTotalTable()
        print(sysname)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "INTERFACE "))
        self.tableWidget_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Interface Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "PHY"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Protocol"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "OutUti"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "InUti"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "InErrors"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "OutErrors"))


    def populateTotalTable(self):

        def uptTable():
            host_mapping = {
                0: "R1",  # Supponiamo che l'indice 0 rappresenti l'host 10.100.0.5
                1: "R3",  # Supponiamo che l'indice 1 rappresenti l'host 10.100.0.7
                2: "R2",  # Supponiamo che l'indice 2 rappresenti l'host 10.100.0.8
            }

            while True:
                # Ottieni dati da tutti gli host
                hosts = ["10.100.0.5", "10.100.0.7", "10.100.0.8"]
                all_interfaces = []

                for host in hosts:
                    connection = Connection()
                    interfaces = connection.getAllInterface(host, "22", "admin", "huawei123", "huawei_vrp")
                    all_interfaces.extend(interfaces)

                self.tableWidget_2.setRowCount(0)
                for row, interface in enumerate(all_interfaces):
                    self.tableWidget_2.insertRow(row)
                    host_label = host_mapping.get(row, "")  # Utilizza l'indice dell'oggetto per identificare l'host
                    self.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(host_label))
                    self.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(interface.phy))
                    self.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(interface.protocol))
                    self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(interface.InUti))
                    self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(interface.OutUti))
                    self.tableWidget_2.setItem(row, 5, QtWidgets.QTableWidgetItem(interface.inErrors))
                    self.tableWidget_2.setItem(row, 6, QtWidgets.QTableWidgetItem(interface.outErrors))

                    time.sleep(5)

        update_thread = threading.Thread(target=uptTable)
        update_thread.daemon = True  # Imposta il thread come daemon per terminarlo quando si chiude l'applicazione
        update_thread.start()

    def showTracert(self, sysname):
        try:
            connectionTrace = Connection()
            output = connectionTrace.tracertRoute(sysname)
            self.label.setText(output)
        except Exception as e:
            # Gestione dell'eccezione, ad esempio, puoi impostare un messaggio di errore sulla label
            self.label.setText("Errore nella connessione SSH: " + str(e))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inflogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 650, 471))
        self.widget.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 471))
        self.label.setStyleSheet("border-image: url(:/image/venv/rec/images/img_xe.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_login = QtWidgets.QPushButton(self.widget)
        self.bt_login.setGeometry(QtCore.QRect(430, 330, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_login.setFont(font)
        self.bt_login.setStyleSheet("QPushButton#bt_login {\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#bt_login:hover {\n"
"    background-color: rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton#bt_login:pressed {\n"
"    background-color: rgb(85, 85, 0);\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.bt_login.setObjectName("bt_login")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(370, 160, 40, 40))
        self.label_3.setStyleSheet("\n"
"border-image: url(:/image/venv/rec/icons/user (1).png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(370, 230, 40, 40))
        self.label_4.setStyleSheet("border-image: url(:/image/venv/rec/icons/padlock.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tx_user = QtWidgets.QLineEdit(self.widget)
        self.tx_user.setGeometry(QtCore.QRect(420, 150, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tx_user.setFont(font)
        self.tx_user.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tx_user.setObjectName("tx_user")
        self.tx_pass = QtWidgets.QLineEdit(self.widget)
        self.tx_pass.setGeometry(QtCore.QRect(420, 220, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tx_pass.setFont(font)
        self.tx_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tx_pass.setObjectName("tx_pass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.bt_login.setText(_translate("MainWindow", "ĐĂNG NHẬP"))
import rec


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

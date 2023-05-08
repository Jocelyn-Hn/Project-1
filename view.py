# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_mainmenu = QtWidgets.QLabel(self.centralwidget)
        self.label_mainmenu.setGeometry(QtCore.QRect(70, 10, 371, 41))
        self.label_mainmenu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mainmenu.setObjectName("label_mainmenu")
        self.label_cookie = QtWidgets.QLabel(self.centralwidget)
        self.label_cookie.setGeometry(QtCore.QRect(70, 60, 131, 16))
        self.label_cookie.setObjectName("label_cookie")
        self.label_sandwich = QtWidgets.QLabel(self.centralwidget)
        self.label_sandwich.setGeometry(QtCore.QRect(70, 100, 131, 16))
        self.label_sandwich.setObjectName("label_sandwich")
        self.label_water = QtWidgets.QLabel(self.centralwidget)
        self.label_water.setGeometry(QtCore.QRect(70, 180, 131, 16))
        self.label_water.setObjectName("label_water")
        self.label_q1 = QtWidgets.QLabel(self.centralwidget)
        self.label_q1.setGeometry(QtCore.QRect(250, 60, 61, 20))
        self.label_q1.setObjectName("label_q1")
        self.label_q2 = QtWidgets.QLabel(self.centralwidget)
        self.label_q2.setGeometry(QtCore.QRect(250, 100, 61, 20))
        self.label_q2.setObjectName("label_q2")
        self.label_q3 = QtWidgets.QLabel(self.centralwidget)
        self.label_q3.setGeometry(QtCore.QRect(250, 180, 61, 20))
        self.label_q3.setObjectName("label_q3")
        self.label_cartmenu = QtWidgets.QLabel(self.centralwidget)
        self.label_cartmenu.setGeometry(QtCore.QRect(70, 260, 371, 31))
        self.label_cartmenu.setText("")
        self.label_cartmenu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cartmenu.setObjectName("label_cartmenu")
        self.output_labels = QtWidgets.QLabel(self.centralwidget)
        self.output_labels.setGeometry(QtCore.QRect(120, 290, 121, 211))
        self.output_labels.setText("")
        self.output_labels.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.output_labels.setObjectName("output_labels")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(140, 510, 71, 31))
        self.button_clear.setObjectName("button_clear")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(290, 510, 71, 31))
        self.button_submit.setObjectName("button_submit")
        self.output_prices = QtWidgets.QLabel(self.centralwidget)
        self.output_prices.setGeometry(QtCore.QRect(260, 290, 131, 211))
        self.output_prices.setText("")
        self.output_prices.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_prices.setObjectName("output_prices")
        self.error_summary = QtWidgets.QLabel(self.centralwidget)
        self.error_summary.setGeometry(QtCore.QRect(170, 290, 161, 211))
        self.error_summary.setText("")
        self.error_summary.setObjectName("error_summary")
        self.label_coffee = QtWidgets.QLabel(self.centralwidget)
        self.label_coffee.setGeometry(QtCore.QRect(70, 220, 131, 16))
        self.label_coffee.setObjectName("label_coffee")
        self.label_q4 = QtWidgets.QLabel(self.centralwidget)
        self.label_q4.setGeometry(QtCore.QRect(250, 220, 61, 20))
        self.label_q4.setObjectName("label_q4")
        self.label_soup = QtWidgets.QLabel(self.centralwidget)
        self.label_soup.setGeometry(QtCore.QRect(70, 140, 131, 16))
        self.label_soup.setObjectName("label_soup")
        self.label_q5 = QtWidgets.QLabel(self.centralwidget)
        self.label_q5.setGeometry(QtCore.QRect(250, 140, 61, 20))
        self.label_q5.setObjectName("label_q5")
        self.input_cookie = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cookie.setGeometry(QtCore.QRect(320, 60, 111, 20))
        self.input_cookie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_cookie.setObjectName("input_cookie")
        self.input_sandwich = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sandwich.setGeometry(QtCore.QRect(320, 100, 111, 20))
        self.input_sandwich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_sandwich.setObjectName("input_sandwich")
        self.input_soup = QtWidgets.QLineEdit(self.centralwidget)
        self.input_soup.setGeometry(QtCore.QRect(320, 140, 111, 20))
        self.input_soup.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_soup.setObjectName("input_soup")
        self.input_water = QtWidgets.QLineEdit(self.centralwidget)
        self.input_water.setGeometry(QtCore.QRect(320, 180, 111, 20))
        self.input_water.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_water.setObjectName("input_water")
        self.input_coffee = QtWidgets.QLineEdit(self.centralwidget)
        self.input_coffee.setGeometry(QtCore.QRect(320, 220, 111, 20))
        self.input_coffee.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_coffee.setObjectName("input_coffee")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mainmenu.setText(_translate("MainWindow", "- - - - - MAIN MENU - - - - -"))
        self.label_cookie.setText(_translate("MainWindow", "Cookie ........... $1.50"))
        self.label_sandwich.setText(_translate("MainWindow", "Sandwich ....... $4.00"))
        self.label_water.setText(_translate("MainWindow", "Water ............ $1.00"))
        self.label_q1.setText(_translate("MainWindow", "Quantity:"))
        self.label_q2.setText(_translate("MainWindow", "Quantity:"))
        self.label_q3.setText(_translate("MainWindow", "Quantity:"))
        self.button_clear.setText(_translate("MainWindow", "CLEAR"))
        self.button_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.label_coffee.setText(_translate("MainWindow", "Coffee ........... $2.50"))
        self.label_q4.setText(_translate("MainWindow", "Quantity:"))
        self.label_soup.setText(_translate("MainWindow", "Soup ............. $3.00"))
        self.label_q5.setText(_translate("MainWindow", "Quantity:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Email.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enter.setGeometry(QtCore.QRect(10, 510, 861, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Enter.setFont(font)
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.textEdit_mail = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_mail.setGeometry(QtCore.QRect(10, 70, 861, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_mail.setFont(font)
        self.textEdit_mail.setObjectName("textEdit_mail")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 450, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(130, 450, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_email.setFont(font)
        self.label_email.setFrameShape(QtWidgets.QFrame.Box)
        self.label_email.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_email.setLineWidth(3)
        self.label_email.setObjectName("label_email")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 26))
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
        self.pushButton_Enter.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "Email 📩"))
        self.label_2.setText(_translate("MainWindow", "Category:"))
        self.label_email.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountForm(object):
    def setupUi(self, AccountForm):
        AccountForm.setObjectName("AccountForm")
        AccountForm.resize(609, 572)
        AccountForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_29 = QtWidgets.QFrame(AccountForm)
        self.line_29.setGeometry(QtCore.QRect(40, 371, 531, 20))
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_31 = QtWidgets.QFrame(AccountForm)
        self.line_31.setGeometry(QtCore.QRect(40, 290, 531, 31))
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_30 = QtWidgets.QFrame(AccountForm)
        self.line_30.setGeometry(QtCore.QRect(40, 140, 531, 16))
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.Account = QtWidgets.QTableWidget(AccountForm)
        self.Account.setGeometry(QtCore.QRect(40, 70, 531, 391))
        self.Account.setStyleSheet("border:0px;\n"
"color: rgb(170, 0, 255);")
        self.Account.setObjectName("Account")
        self.Account.setColumnCount(2)
        self.Account.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Account.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Account.setHorizontalHeaderItem(1, item)
        self.line_33 = QtWidgets.QFrame(AccountForm)
        self.line_33.setGeometry(QtCore.QRect(40, 217, 531, 16))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.pushButton_9 = QtWidgets.QPushButton(AccountForm)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 490, 401, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_15 = QtWidgets.QLabel(AccountForm)
        self.label_15.setGeometry(QtCore.QRect(10, 0, 271, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(AccountForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(570, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.Account.raise_()
        self.line_29.raise_()
        self.line_31.raise_()
        self.line_30.raise_()
        self.line_33.raise_()
        self.pushButton_9.raise_()
        self.label_15.raise_()
        self.closeenterpsw.raise_()

        self.retranslateUi(AccountForm)
        QtCore.QMetaObject.connectSlotsByName(AccountForm)

    def retranslateUi(self, AccountForm):
        _translate = QtCore.QCoreApplication.translate
        AccountForm.setWindowTitle(_translate("AccountForm", "Form"))
        item = self.Account.horizontalHeaderItem(0)
        item.setText(_translate("AccountForm", "Wallet Name"))
        item = self.Account.horizontalHeaderItem(1)
        item.setText(_translate("AccountForm", "Public Address"))
        self.pushButton_9.setText(_translate("AccountForm", "Select"))
        self.label_15.setText(_translate("AccountForm", "Select Account"))


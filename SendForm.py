# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SendForm(object):
    def setupUi(self, SendForm):
        SendForm.setObjectName("SendForm")
        SendForm.resize(467, 489)
        SendForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QtWidgets.QLineEdit(SendForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setToolTip("")
        self.lineEdit_6.setStatusTip("")
        self.lineEdit_6.setWhatsThis("")
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setAccessibleDescription("")
        self.lineEdit_6.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.closeenterpsw = QtWidgets.QPushButton(SendForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(430, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.label_15 = QtWidgets.QLabel(SendForm)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(170, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.line_38 = QtWidgets.QFrame(SendForm)
        self.line_38.setGeometry(QtCore.QRect(130, 80, 271, 10))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.label_7 = QtWidgets.QLabel(SendForm)
        self.label_7.setGeometry(QtCore.QRect(400, 50, 51, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_9 = QtWidgets.QPushButton(SendForm)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 360, 291, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.line_39 = QtWidgets.QFrame(SendForm)
        self.line_39.setGeometry(QtCore.QRect(30, 310, 200, 10))
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(SendForm)
        self.line_40.setGeometry(QtCore.QRect(250, 310, 200, 10))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(SendForm)
        self.line_41.setGeometry(QtCore.QRect(30, 170, 320, 10))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.pushButton_34 = QtWidgets.QPushButton(SendForm)
        self.pushButton_34.setGeometry(QtCore.QRect(360, 130, 41, 41))
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_34.setAutoFillBackground(False)
        self.pushButton_34.setStyleSheet("border:0px;")
        self.pushButton_34.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon1)
        self.pushButton_34.setIconSize(QtCore.QSize(77, 77))
        self.pushButton_34.setAutoDefault(False)
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_36 = QtWidgets.QPushButton(SendForm)
        self.pushButton_36.setGeometry(QtCore.QRect(400, 130, 41, 41))
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_36.setAutoFillBackground(False)
        self.pushButton_36.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon2)
        self.pushButton_36.setIconSize(QtCore.QSize(77, 77))
        self.pushButton_36.setAutoDefault(False)
        self.pushButton_36.setFlat(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.label_51 = QtWidgets.QLabel(SendForm)
        self.label_51.setGeometry(QtCore.QRect(30, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(SendForm)
        self.label_52.setGeometry(QtCore.QRect(150, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")
        self.lineEdit_7 = QtWidgets.QLineEdit(SendForm)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setToolTip("")
        self.lineEdit_7.setStatusTip("")
        self.lineEdit_7.setWhatsThis("")
        self.lineEdit_7.setAccessibleName("")
        self.lineEdit_7.setAccessibleDescription("")
        self.lineEdit_7.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_53 = QtWidgets.QLabel(SendForm)
        self.label_53.setGeometry(QtCore.QRect(30, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_53.setObjectName("label_53")
        self.radioButton = QtWidgets.QRadioButton(SendForm)
        self.radioButton.setGeometry(QtCore.QRect(30, 230, 89, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton.setStyleSheet("border:0px;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(SendForm)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 230, 89, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_2.setStyleSheet("border:0px;")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(SendForm)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 230, 89, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_3.setStyleSheet("border:0px;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(SendForm)
        self.radioButton_4.setGeometry(QtCore.QRect(330, 230, 89, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_4.setStyleSheet("border:0px;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_54 = QtWidgets.QLabel(SendForm)
        self.label_54.setGeometry(QtCore.QRect(30, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(SendForm)
        self.label_55.setGeometry(QtCore.QRect(250, 260, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_55.setObjectName("label_55")
        self.lineEdit_8 = QtWidgets.QLineEdit(SendForm)
        self.lineEdit_8.setGeometry(QtCore.QRect(50, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setToolTip("")
        self.lineEdit_8.setStatusTip("")
        self.lineEdit_8.setWhatsThis("")
        self.lineEdit_8.setAccessibleName("")
        self.lineEdit_8.setAccessibleDescription("")
        self.lineEdit_8.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(SendForm)
        self.lineEdit_9.setGeometry(QtCore.QRect(270, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setToolTip("")
        self.lineEdit_9.setStatusTip("")
        self.lineEdit_9.setWhatsThis("")
        self.lineEdit_9.setAccessibleName("")
        self.lineEdit_9.setAccessibleDescription("")
        self.lineEdit_9.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.retranslateUi(SendForm)
        QtCore.QMetaObject.connectSlotsByName(SendForm)

    def retranslateUi(self, SendForm):
        _translate = QtCore.QCoreApplication.translate
        SendForm.setWindowTitle(_translate("SendForm", "Form"))
        self.label_15.setText(_translate("SendForm", "Send"))
        self.label_7.setText(_translate("SendForm", "WTCT"))
        self.pushButton_9.setText(_translate("SendForm", "Send"))
        self.label_51.setText(_translate("SendForm", "Address:"))
        self.label_52.setText(_translate("SendForm", "0 WTCT"))
        self.lineEdit_7.setPlaceholderText(_translate("SendForm", "Enter Recipient Address"))
        self.label_53.setText(_translate("SendForm", "Set the gas fee:"))
        self.radioButton.setText(_translate("SendForm", "Economic"))
        self.radioButton_2.setText(_translate("SendForm", "Standard"))
        self.radioButton_3.setText(_translate("SendForm", "Quick"))
        self.radioButton_4.setText(_translate("SendForm", "Custom"))
        self.label_54.setText(_translate("SendForm", "Gas Limit:"))
        self.label_55.setText(_translate("SendForm", "Gas price:"))
        self.lineEdit_8.setText(_translate("SendForm", "200000"))
        self.lineEdit_9.setText(_translate("SendForm", "0.000000036"))


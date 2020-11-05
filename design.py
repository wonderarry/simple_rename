# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 414)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(791, 414))
        MainWindow.setMaximumSize(QtCore.QSize(791, 414))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_list = QtWidgets.QListWidget(self.centralwidget)
        self.main_list.setGeometry(QtCore.QRect(150, 20, 631, 341))
        self.main_list.setObjectName("main_list")
        self.move_up = QtWidgets.QPushButton(self.centralwidget)
        self.move_up.setGeometry(QtCore.QRect(10, 22, 121, 31))
        self.move_up.setObjectName("move_up")
        self.move_down = QtWidgets.QPushButton(self.centralwidget)
        self.move_down.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.move_down.setObjectName("move_down")
        self.add_elem = QtWidgets.QPushButton(self.centralwidget)
        self.add_elem.setGeometry(QtCore.QRect(10, 190, 121, 31))
        self.add_elem.setObjectName("add_elem")
        self.rem_elem = QtWidgets.QPushButton(self.centralwidget)
        self.rem_elem.setGeometry(QtCore.QRect(10, 260, 121, 31))
        self.rem_elem.setObjectName("rem_elem")
        self.clear_list = QtWidgets.QPushButton(self.centralwidget)
        self.clear_list.setGeometry(QtCore.QRect(10, 310, 121, 31))
        self.clear_list.setObjectName("clear_list")
        self.name_mask = QtWidgets.QLineEdit(self.centralwidget)
        self.name_mask.setGeometry(QtCore.QRect(200, 380, 211, 20))
        self.name_mask.setObjectName("name_mask")
        self.name_incr = QtWidgets.QSpinBox(self.centralwidget)
        self.name_incr.setGeometry(QtCore.QRect(480, 380, 51, 22))
        self.name_incr.setMinimum(1)
        self.name_incr.setMaximum(1000)
        self.name_incr.setObjectName("name_incr")
        self.do_execute = QtWidgets.QPushButton(self.centralwidget)
        self.do_execute.setGeometry(QtCore.QRect(550, 375, 231, 31))
        self.do_execute.setObjectName("do_execute")
        self.name_descript = QtWidgets.QLineEdit(self.centralwidget)
        self.name_descript.setGeometry(QtCore.QRect(10, 380, 181, 20))
        self.name_descript.setFrame(False)
        self.name_descript.setReadOnly(True)
        self.name_descript.setObjectName("name_descript")
        self.sort_list_asc = QtWidgets.QPushButton(self.centralwidget)
        self.sort_list_asc.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.sort_list_asc.setObjectName("sort_list_asc")
        self.sort_list_desc = QtWidgets.QPushButton(self.centralwidget)
        self.sort_list_desc.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.sort_list_desc.setObjectName("sort_list_desc")
        self.name_base = QtWidgets.QSpinBox(self.centralwidget)
        self.name_base.setGeometry(QtCore.QRect(420, 380, 51, 22))
        self.name_base.setMinimum(0)
        self.name_base.setMaximum(1000)
        self.name_base.setProperty("value", 0)
        self.name_base.setObjectName("name_base")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Renaming Tool"))
        self.move_up.setText(_translate("MainWindow", "Move up"))
        self.move_down.setText(_translate("MainWindow", "Move down"))
        self.add_elem.setText(_translate("MainWindow", "Add element"))
        self.rem_elem.setText(_translate("MainWindow", "Remove element"))
        self.clear_list.setText(_translate("MainWindow", "Clear the list"))
        self.do_execute.setText(_translate("MainWindow", "Choose folder and execute"))
        self.name_descript.setText(_translate("MainWindow", "Input the name, base and increment:"))
        self.sort_list_asc.setText(_translate("MainWindow", "Sort the list(asc.)"))
        self.sort_list_desc.setText(_translate("MainWindow", "Sort the list(desc.)"))

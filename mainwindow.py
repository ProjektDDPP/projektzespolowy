# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Mar 10 21:41:23 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 567)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.excelWidget = QtGui.QTableWidget(self.centralwidget)
        self.excelWidget.setMinimumSize(QtCore.QSize(0, 400))
        self.excelWidget.setObjectName("excelWidget")
        self.excelWidget.setColumnCount(0)
        self.excelWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.excelWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setMinimumSize(QtCore.QSize(0, 50))
        self.listView.setMaximumSize(QtCore.QSize(16777215, 150))
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 20))
        self.menubar.setObjectName("menubar")
        self.menuLol = QtGui.QMenu(self.menubar)
        self.menuLol.setObjectName("menuLol")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWczytaj_plik = QtGui.QAction(MainWindow)
        self.actionWczytaj_plik.setObjectName("actionWczytaj_plik")
        self.actionZapisz_jako_pdf = QtGui.QAction(MainWindow)
        self.actionZapisz_jako_pdf.setObjectName("actionZapisz_jako_pdf")
        self.actionWyjd = QtGui.QAction(MainWindow)
        self.actionWyjd.setObjectName("actionWyjd")
        self.menuLol.addAction(self.actionWczytaj_plik)
        self.menuLol.addAction(self.actionZapisz_jako_pdf)
        self.menuLol.addAction(self.actionWyjd)
        self.menubar.addAction(self.menuLol.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Odchylenie standardowe", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Mediana", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Korelacja", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Kowariancja", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Rozk. Prawdopodobieństwa", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLol.setTitle(QtGui.QApplication.translate("MainWindow", "Plik", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWczytaj_plik.setText(QtGui.QApplication.translate("MainWindow", "Wczytaj plik", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZapisz_jako_pdf.setText(QtGui.QApplication.translate("MainWindow", "Zapisz jako pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWyjd.setText(QtGui.QApplication.translate("MainWindow", "Wyjdź", None, QtGui.QApplication.UnicodeUTF8))


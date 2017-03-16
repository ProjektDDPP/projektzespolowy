# -*- coding: UTF-8 -*-

import sys
import xlrd
from PySide import QtGui
from PySide import QtCore
from mainwindow import Ui_MainWindow

class mainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.actionWczytaj_plik, QtCore.SIGNAL('triggered()'), self, QtCore.SLOT('loadFile()'))
        self.connect(self.ui.actionZapisz_jako_pdf, QtCore.SIGNAL('triggered()'), self, QtCore.SLOT('saveFile()'))

        self.show()

    def loadFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print fname
        book = xlrd.open_workbook(fname[0])
        sheet_name = book.sheet_names()[0]
        arkusz = book.sheet_by_name(sheet_name)

        self.ui.excelWidget.setRowCount(arkusz.nrows);
        self.ui.excelWidget.setColumnCount(arkusz.ncols);

        for row in range(0, arkusz.nrows):
            valuesInRow = arkusz.row_values(row)
            for col in range(0, arkusz.ncols):
                self.ui.excelWidget.setItem(row, col, QtGui.QTableWidgetItem(str(valuesInRow[col])))

    def saveFile(self):
        #fname = QtGui.QFileDialog.getSaveFileName(self, 'Open file', '/home')
        #file = open(fname[0], 'w')
        self.printToPdf()

    def printToPdf(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setPageSize(QtGui.QPrinter.Letter)
        printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        printer.setOutputFileName("treeTest.pdf")
        painter = QtGui.QPainter()
        painter.begin(printer)
        try:
            self.ui.listView.render(painter, QtCore.QPoint())
        finally:
            painter.end()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

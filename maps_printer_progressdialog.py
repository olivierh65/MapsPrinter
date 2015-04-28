# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maps_printer_progressdialog.ui'
#
# Created: Mon Apr 27 01:49:27 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mapsPrinterProgress(object):
    def setupUi(self, mapsPrinterProgress):
        mapsPrinterProgress.setObjectName(_fromUtf8("mapsPrinterProgress"))
        mapsPrinterProgress.resize(281, 131)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mapsPrinterProgress.sizePolicy().hasHeightForWidth())
        mapsPrinterProgress.setSizePolicy(sizePolicy)
        mapsPrinterProgress.setMinimumSize(QtCore.QSize(0, 0))
        mapsPrinterProgress.setSizeIncrement(QtCore.QSize(0, 0))
        mapsPrinterProgress.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapsPrinter/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mapsPrinterProgress.setWindowIcon(icon)
        mapsPrinterProgress.setSizeGripEnabled(False)
        mapsPrinterProgress.setModal(True)
        self.gridLayout = QtGui.QGridLayout(mapsPrinterProgress)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.buttonBox = QtGui.QDialogButtonBox(mapsPrinterProgress)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 6, 0, 1, 1)
        self.printinglabel = QtGui.QLabel(mapsPrinterProgress)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.printinglabel.sizePolicy().hasHeightForWidth())
        self.printinglabel.setSizePolicy(sizePolicy)
        self.printinglabel.setMinimumSize(QtCore.QSize(0, 20))
        self.printinglabel.setObjectName(_fromUtf8("printinglabel"))
        self.gridLayout_3.addWidget(self.printinglabel, 0, 0, 1, 1)
        self.printBar = QtGui.QProgressBar(mapsPrinterProgress)
        self.printBar.setProperty("value", 0)
        self.printBar.setObjectName(_fromUtf8("printBar"))
        self.gridLayout_3.addWidget(self.printBar, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.general = QtGui.QLabel(mapsPrinterProgress)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general.sizePolicy().hasHeightForWidth())
        self.general.setSizePolicy(sizePolicy)
        self.general.setMinimumSize(QtCore.QSize(0, 20))
        self.general.setFrameShape(QtGui.QFrame.NoFrame)
        self.general.setObjectName(_fromUtf8("general"))
        self.horizontalLayout.addWidget(self.general)
        self.generalBar = QtGui.QProgressBar(mapsPrinterProgress)
        self.generalBar.setMinimumSize(QtCore.QSize(0, 20))
        self.generalBar.setProperty("value", 0)
        self.generalBar.setObjectName(_fromUtf8("generalBar"))
        self.horizontalLayout.addWidget(self.generalBar)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 3, 1)

        self.retranslateUi(mapsPrinterProgress)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), mapsPrinterProgress.close)
        QtCore.QMetaObject.connectSlotsByName(mapsPrinterProgress)

    def retranslateUi(self, mapsPrinterProgress):
        mapsPrinterProgress.setWindowTitle(_translate("mapsPrinterProgress", "Maps Printer", None))
        self.printinglabel.setText(_translate("mapsPrinterProgress", "Exporting ...", None))
        self.general.setText(_translate("mapsPrinterProgress", "Total export", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mapsPrinterProgress = QtGui.QDialog()
    ui = Ui_mapsPrinterProgress()
    ui.setupUi(mapsPrinterProgress)
    mapsPrinterProgress.show()
    sys.exit(app.exec_())


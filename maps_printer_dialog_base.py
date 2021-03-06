# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maps_printer_dialog_base.ui'
#
# Created: Thu Jul 30 01:03:16 2015
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

class Ui_mapsPrinter(object):
    def setupUi(self, mapsPrinter):
        mapsPrinter.setObjectName(_fromUtf8("mapsPrinter"))
        mapsPrinter.resize(375, 355)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mapsPrinter.sizePolicy().hasHeightForWidth())
        mapsPrinter.setSizePolicy(sizePolicy)
        mapsPrinter.setMinimumSize(QtCore.QSize(320, 340))
        mapsPrinter.setSizeIncrement(QtCore.QSize(0, 0))
        mapsPrinter.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapsPrinter/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mapsPrinter.setWindowIcon(icon)
        mapsPrinter.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(mapsPrinter)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(10, 12, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(mapsPrinter)
        self.checkBox.setEnabled(True)
        self.checkBox.setWhatsThis(_fromUtf8(""))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.updater = QtGui.QPushButton(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updater.sizePolicy().hasHeightForWidth())
        self.updater.setSizePolicy(sizePolicy)
        self.updater.setMinimumSize(QtCore.QSize(80, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapsPrinter/icons/action_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updater.setIcon(icon1)
        self.updater.setObjectName(_fromUtf8("updater"))
        self.gridLayout.addWidget(self.updater, 0, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.printBar = QtGui.QProgressBar(mapsPrinter)
        self.printBar.setProperty("value", 0)
        self.printBar.setObjectName(_fromUtf8("printBar"))
        self.horizontalLayout.addWidget(self.printBar)
        self.exportButton = QtGui.QPushButton(mapsPrinter)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        self.buttonBox = QtGui.QDialogButtonBox(mapsPrinter)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 3)
        self.composerList = QtGui.QListWidget(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.composerList.sizePolicy().hasHeightForWidth())
        self.composerList.setSizePolicy(sizePolicy)
        self.composerList.setSizeIncrement(QtCore.QSize(0, 0))
        self.composerList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.composerList.setMouseTracking(False)
        self.composerList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.composerList.setAcceptDrops(True)
        self.composerList.setToolTip(_fromUtf8(""))
        self.composerList.setWhatsThis(_fromUtf8(""))
        self.composerList.setAlternatingRowColors(True)
        self.composerList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.composerList.setResizeMode(QtGui.QListView.Fixed)
        self.composerList.setObjectName(_fromUtf8("composerList"))
        self.gridLayout.addWidget(self.composerList, 2, 0, 1, 3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.printinglabel = QtGui.QLabel(mapsPrinter)
        self.printinglabel.setEnabled(True)
        self.printinglabel.setObjectName(_fromUtf8("printinglabel"))
        self.horizontalLayout_6.addWidget(self.printinglabel)
        self.pageBar = QtGui.QProgressBar(mapsPrinter)
        self.pageBar.setProperty("value", 0)
        self.pageBar.setObjectName(_fromUtf8("pageBar"))
        self.horizontalLayout_6.addWidget(self.pageBar)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.formatBox = QtGui.QComboBox(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatBox.sizePolicy().hasHeightForWidth())
        self.formatBox.setSizePolicy(sizePolicy)
        self.formatBox.setMinimumSize(QtCore.QSize(0, 23))
        self.formatBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.formatBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.formatBox.setWhatsThis(_fromUtf8(""))
        self.formatBox.setObjectName(_fromUtf8("formatBox"))
        self.horizontalLayout_2.addWidget(self.formatBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.path = QtGui.QLineEdit(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setSizeIncrement(QtCore.QSize(0, 0))
        self.path.setToolTip(_fromUtf8(""))
        self.path.setWhatsThis(_fromUtf8(""))
        self.path.setObjectName(_fromUtf8("path"))
        self.horizontalLayout_3.addWidget(self.path)
        self.browser = QtGui.QPushButton(mapsPrinter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setMinimumSize(QtCore.QSize(100, 23))
        self.browser.setObjectName(_fromUtf8("browser"))
        self.horizontalLayout_3.addWidget(self.browser)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)

        self.retranslateUi(mapsPrinter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mapsPrinter.reject)
        QtCore.QMetaObject.connectSlotsByName(mapsPrinter)
        mapsPrinter.setTabOrder(self.checkBox, self.updater)
        mapsPrinter.setTabOrder(self.updater, self.composerList)
        mapsPrinter.setTabOrder(self.composerList, self.path)
        mapsPrinter.setTabOrder(self.path, self.browser)
        mapsPrinter.setTabOrder(self.browser, self.formatBox)
        mapsPrinter.setTabOrder(self.formatBox, self.exportButton)
        mapsPrinter.setTabOrder(self.exportButton, self.buttonBox)

    def retranslateUi(self, mapsPrinter):
        mapsPrinter.setWindowTitle(_translate("mapsPrinter", "Maps Printer", None))
        self.checkBox.setToolTip(_translate("mapsPrinter", "Check all the composers", None))
        self.checkBox.setText(_translate("mapsPrinter", "Check All", None))
        self.updater.setToolTip(_translate("mapsPrinter", "Update composer list", None))
        self.updater.setText(_translate("mapsPrinter", "Update", None))
        self.exportButton.setText(_translate("mapsPrinter", "Export", None))
        self.printinglabel.setText(_translate("mapsPrinter", "Exporting...", None))
        self.label.setText(_translate("mapsPrinter", "Output File Format", None))
        self.formatBox.setToolTip(_translate("mapsPrinter", "Choose the output file format", None))
        self.browser.setToolTip(_translate("mapsPrinter", "Choose the output folder", None))
        self.browser.setText(_translate("mapsPrinter", "Br&owse...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mapsPrinter = QtGui.QDialog()
    ui = Ui_mapsPrinter()
    ui.setupUi(mapsPrinter)
    mapsPrinter.show()
    sys.exit(app.exec_())


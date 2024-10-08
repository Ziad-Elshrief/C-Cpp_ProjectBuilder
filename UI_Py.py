# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gcc_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(430, 410))
        MainWindow.setStyleSheet("QMenu::item:disabled{\n"
"color: gray;\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(55,149,189);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(92, 104, 102);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dirButton = QtWidgets.QPushButton(self.centralwidget)
        self.dirButton.setGeometry(QtCore.QRect(280, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dirButton.setFont(font)
        self.dirButton.setStyleSheet("")
        self.dirButton.setObjectName("dirButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 77, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(80,140,155)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.exeLabel = QtWidgets.QLabel(self.centralwidget)
        self.exeLabel.setGeometry(QtCore.QRect(250, 70, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exeLabel.setFont(font)
        self.exeLabel.setObjectName("exeLabel")
        self.InfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.InfoLabel.setGeometry(QtCore.QRect(20, 120, 81, 31))
        self.InfoLabel.setStyleSheet("QLabel#InfoLabel {\n"
"border-bottom:solid;\n"
"\n"
"    border-width: 2px;\n"
"border-top:none;\n"
"border-bottom-color:  rgb(80,140,155);\n"
"}")
        self.InfoLabel.setObjectName("InfoLabel")
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(110, 120, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setStyleSheet("QLabel#ResultLabel{\n"
"    background-color: black;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(80,140,155)\n"
"}")
        self.ResultLabel.setObjectName("ResultLabel")
        self.DirLabel = QtWidgets.QLabel(self.centralwidget)
        self.DirLabel.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.DirLabel.setFont(font)
        self.DirLabel.setStyleSheet("QLabel#DirLabel {\n"
"border-bottom:solid;\n"
"\n"
"    border-width: 2px;\n"
"border-top:none;\n"
"border-bottom-color:  rgb(80,140,155);\n"
"}")
        self.DirLabel.setObjectName("DirLabel")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(20, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showButton.setFont(font)
        self.showButton.setObjectName("showButton")
        self.buildButton = QtWidgets.QPushButton(self.centralwidget)
        self.buildButton.setGeometry(QtCore.QRect(150, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buildButton.setFont(font)
        self.buildButton.setObjectName("buildButton")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(280, 330, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 160, 401, 151))
        self.scrollArea.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 401, 151))
        self.scrollAreaWidgetContents.setMouseTracking(False)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ErrorLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setMouseTracking(False)
        self.ErrorLabel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.ErrorLabel.setStyleSheet("QLabel#ErrorLabel{\n"
"    background-color: black;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(80,140,155)\n"
"}")
        self.ErrorLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ErrorLabel.setLineWidth(2)
        self.ErrorLabel.setText("")
        self.ErrorLabel.setWordWrap(True)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.verticalLayout.addWidget(self.ErrorLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(20, 70, 61, 31))
        self.NameLabel.setStyleSheet("QLabel#NameLabel {\n"
"border-bottom:solid;\n"
"\n"
"    border-width: 2px;\n"
"border-top:none;\n"
"border-bottom-color:  rgb(80,140,155);\n"
"}")
        self.NameLabel.setObjectName("NameLabel")
        self.lineEdit.raise_()
        self.exeLabel.raise_()
        self.InfoLabel.raise_()
        self.ResultLabel.raise_()
        self.DirLabel.raise_()
        self.showButton.raise_()
        self.buildButton.raise_()
        self.runButton.raise_()
        self.scrollArea.raise_()
        self.NameLabel.raise_()
        self.dirButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionBuild = QtWidgets.QAction(MainWindow)
        self.actionBuild.setObjectName("actionBuild")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "C/C++ Project Builder"))
        self.dirButton.setText(_translate("MainWindow", "Choose Directory"))
        self.lineEdit.setText(_translate("MainWindow", "Output"))
        self.exeLabel.setText(_translate("MainWindow", ".exe"))
        self.InfoLabel.setText(_translate("MainWindow", "Building Result:"))
        self.ResultLabel.setText(_translate("MainWindow", "Not built yet"))
        self.DirLabel.setText(_translate("MainWindow", "Choose the folder conataning the project"))
        self.showButton.setText(_translate("MainWindow", "Show in folder"))
        self.buildButton.setText(_translate("MainWindow", "Build"))
        self.runButton.setText(_translate("MainWindow", "Run Output"))
        self.NameLabel.setText(_translate("MainWindow", "EXE Name:"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionBuild.setText(_translate("MainWindow", "Build"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

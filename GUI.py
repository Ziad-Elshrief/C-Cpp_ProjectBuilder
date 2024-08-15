from PyQt5.QtWidgets import QMainWindow , QApplication ,QLabel , QPushButton 
from PyQt5.QtWidgets import  QFileDialog , QLineEdit ,QShortcut , QMenu , QAction 
from PyQt5.QtGui import QIcon , QKeySequence , QPalette , QColor
from PyQt5.QtCore import Qt

import sys

#Import Class Responsible for building
from Builder import buildTool

#Import UI Class from Qt Designer 
from UI_Py import Ui_MainWindow

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #Creating object from buildTool class 
        self.buildTool = buildTool()
        
        #Creating object from ui class 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Change App Icon
        try:
            #To use temp file created from PyInstaller in case of using program.exe 
            base_path = sys._MEIPASS
        except Exception:
            base_path = self.buildTool.program_path
        self.setWindowIcon(QIcon(f"{base_path}\\logo.png"))
        
        #calling function to get widgets
        self.getWidgets()

        #Disabling buttons before building
        self.showButton.setEnabled(False)
        self.runButton.setEnabled(False)

        #call the method responsible for creating Menu Bar 
        self.createMenu()

        #Call the method responsible for keyboard shortcuts
        self.createShortcuts()
       
        #Call the method responsible for connecting each button to its job
        self.connectButtons()
       
        #show the app main window
        self.show()

        

    #Choose Directory Button method
    def chooseDir(self):
        #Emptying labels when choosing another directory
        self.ErrorLabel.setText("")
        self.ResultLabel.setText("")

        self.buildTool.original_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.DirLabel.setText(self.buildTool.original_path)
        if self.buildTool.checkDir():
            #Enabling show button after choosing correct directory
            self.showButton.setEnabled(True)
            #Enabling show in folder shortcut
            self.showShortcut.setEnabled(True)
            #Enabling show in folder menu Action
            self.showInFolderAction.setEnabled(True)

        else:
            self.DirLabel.setText("Path doesn't exist")
            #Disabling show button until a directory is chosen
            self.showButton.setEnabled(False)
            #Disable show in folder shortcut 
            self.showShortcut.setEnabled(False)
            #Disabling show in folder menu Action
            self.showInFolderAction.setEnabled(False)

    #Show in folder button method
    def showInFolder(self):
        if not self.buildTool.openFolder():
            self.ResultLabel.setText("Error showing in folder")

    #Build button method        
    def buildProject(self):
            #Emptying Error Label when building again
            self.ErrorLabel.setText("")

            self.ResultLabel.setText("Building .....")

            #Call the build method
            self.buildResult=self.buildTool.build(self.OutputLine.text())
            self.ResultLabel.setText(self.buildResult)
            #Check the outcome of the building process
            if self.buildResult.endswith("Build Complete"):
                #Enabling Run Button if build process is successful
                self.runButton.setEnabled(True)
                #Enabling run shortcut if build process is successful
                self.runShortcut.setEnabled(True)
                #Enabling run menu action if build process is successful
                self.runAction.setEnabled(True) 
            elif self.buildResult == "Error":
                #Disable run button ,action and shortcut
                self.runButton.setEnabled(False)
                self.runShortcut.setEnabled(False)
                self.runAction.setEnabled(False)
                #Show in app that the cmd returned with error
                self.ResultLabel.setText("Error executing command")
                #Show error Content on Error Label
                self.ErrorLabel.setText(self.buildTool.getError())
                #Making the text selectable so the error can be copied
                self.ErrorLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
            else:
                #Disable run button and shortcut
                self.runButton.setEnabled(False)
                self.runShortcut.setEnabled(False)
                self.runAction.setEnabled(False)



    #Create keyboard shortcuts 
    def createShortcuts(self):
        #Ctrl+B to build project
        self.buildShortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_B), self)
        self.buildShortcut.activated.connect(self.buildProject)

        #Ctrl+F5 to run output
        self.runShortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F5), self)
        self.runShortcut.activated.connect(self.buildTool.runOutput)
        #Disable it until a building is done
        self.runShortcut.setEnabled(False)

        #Ctrl+I to show in folder
        self.showShortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_I), self)
        self.showShortcut.activated.connect(self.showInFolder)
        #Disable it until a directory is chosen
        self.showShortcut.setEnabled(False)

        #Ctrl+H to open help page
        self.helpShortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_H), self)
        self.helpShortcut.activated.connect(self.buildTool.helpPage)

    #get Widgets from ui class using findChild
    def getWidgets(self):
        self.exeLabel= self.findChild(QLabel,"exeLabel")
        self.InfoLabel= self.findChild(QLabel,"InfoLabel")
        self.ResultLabel= self.findChild(QLabel,"ResultLabel")
        self.DirLabel=self.findChild(QLabel,"DirLabel")

        self.ErrorLabel=self.findChild(QLabel,"ErrorLabel")


        self.menuHelp=self.findChild(QMenu,"menuHelp")
        self.menuEdit=self.findChild(QMenu,"menuEdit")
        self.menuFile=self.findChild(QMenu,"menuFile")

        self.OutputLine=self.findChild(QLineEdit,"lineEdit")
       
        self.dirButton= self.findChild(QPushButton,"dirButton")
        self.showButton= self.findChild(QPushButton,"showButton")
        self.buildButton= self.findChild(QPushButton,"buildButton")
        self.runButton= self.findChild(QPushButton,"runButton")

    #Connect each button to its method
    def connectButtons(self):
        self.dirButton.clicked.connect(self.chooseDir)
        self.showButton.clicked.connect(self.showInFolder)
        self.buildButton.clicked.connect(self.buildProject)
        self.runButton.clicked.connect(self.buildTool.runOutput)

    #Creating Menu Bar 
    def createMenu(self):
        #Creating help Menu
        self.helpPageAction = QAction("&Help page", self)
        self.menuHelp.addAction(self.helpPageAction)
        self.helpPageAction.triggered.connect(self.buildTool.helpPage)

        #Creating file menu
        self.chooseDirAction = QAction("&Choose directory",self)
        self.menuFile.addAction(self.chooseDirAction)
        self.chooseDirAction.triggered.connect(self.chooseDir)

        self.showInFolderAction = QAction("&Show in folder",self)
        self.menuFile.addAction(self.showInFolderAction)
        self.showInFolderAction.triggered.connect(self.showInFolder)
        #Disable it until a directory is chosen
        self.showInFolderAction.setEnabled(False)

        #Creating edit menu
        self.buildAction = QAction("&Build",self)
        self.menuEdit.addAction( self.buildAction)
        self.buildAction.triggered.connect(self.buildProject)
        
        self.runAction  = QAction("&Run output",self)
        self.menuEdit.addAction( self.runAction)
        self.runAction.triggered.connect(self.buildTool.runOutput)
        #Disabling it until building is done
        self.runAction.setEnabled(False)


#Intialize and start app
app = QApplication(sys.argv)

#Choosing the style of the application
app.setStyle("Fusion")


#Creating a color palette
palette = QPalette()
palette.setColor(QPalette.Window, QColor(3,28,37))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Button,QColor(26,72,112))
palette.setColor(QPalette.ButtonText,  Qt.white)
palette.setColor(QPalette.Base,QColor(26,72,112))
palette.setColor(QPalette.Text,Qt.white)
palette.setColor(QPalette.Highlight, Qt.white)
palette.setColor(QPalette.HighlightedText, QColor(26,72,112))
palette.setColor(QPalette.ToolTipBase, QColor(80,140,155))
palette.setColor(QPalette.ToolTipText, Qt.white)

app.setPalette(palette) 

UIWindow = UI()
sys.exit(app.exec_())

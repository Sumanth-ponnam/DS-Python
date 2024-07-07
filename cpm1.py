import sys
import os
from cpm import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.dispgraph)
     self.ui.pushButton_2.clicked.connect(self.idcpath)
     self.ui.pushButton_3.clicked.connect(self.ducpath)
     self.ui.pushButton_5.clicked.connect(self.snanal)
     self.ui.pushButton_6.clicked.connect(self.lranal)
 
  def dispgraph(self):
    os.system("python graph1.py")       

  def idcpath(self):
    os.system("python cpath2.py")

  def ducpath(self):
    os.system("python cpath1.py")

  def snanal(self):
    os.system("python -W ignore delivery1.py")

  def lranal(self):
    os.system("python -W ignore delivery2.py")
	
     
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

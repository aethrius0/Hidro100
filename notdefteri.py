import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.yazi_alani=QtWidgets.QTextEdit(self)
        self.yazi_alani.setGeometry(10,10,350,400)
    
        self.buton_kaydet=QtWidgets.QPushButton("Kaydet",self)
        self.buton_temizle=QtWidgets.QPushButton("Temizle",self)
        
        self.buton_kaydet.move(200,420)
        self.buton_temizle.move(100,420)
        
        
        
        self.show()







app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())    

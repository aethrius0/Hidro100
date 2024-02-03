import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.yazi_alani=QtWidgets.QTextEdit(self)
        self.yazi_alani.setGeometry(10,10,350,400)
        
        #Sağ tarafta kaydedilen notların olduğu kısım
        self.kayitli_kutucuk=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk.move(400,10)
        self.kayitli_kutucuk.setGeometry(400,10,200,80)
        
        self.kayitli_kutucuk_2=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_2.setGeometry(400,100,200,80)
        
        self.kayitli_kutucuk_3=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_3.setGeometry(400,190,200,80)
        
        self.kayitli_kutucuk_4=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_4.setGeometry(400,280,200,80)
        #---------------------------------------------------------
        
        
        
        self.buton_kaydet=QtWidgets.QPushButton("Kaydet",self)
        self.buton_temizle=QtWidgets.QPushButton("Temizle",self)
        
        self.buton_kaydet.move(200,420)
        self.buton_temizle.move(100,420)
        
        self.buton_kaydet.clicked.connect(self.kaydet_clicked)

        self.show()
    
        
    def kaydet_clicked(self):
        yazi=self.yazi_alani.toPlainText()
        if not self.kayitli_kutucuk.toPlainText():
            self.kayitli_kutucuk.append(yazi)
            self.yazi_alani.clear()
        
        elif not self.kayitli_kutucuk_2.toPlainText():
            self.kayitli_kutucuk_2.append(yazi)
            self.yazi_alani.clear()
        
        elif not self.kayitli_kutucuk_3.toPlainText():
            self.kayitli_kutucuk_3.append(yazi)
            self.yazi_alani.clear()
        
        elif not self.kayitli_kutucuk_4.toPlainText():
            self.kayitli_kutucuk_4.append(yazi)
            self.yazi_alani.clear()
        
        else:
            pass    
        
        
    


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())    

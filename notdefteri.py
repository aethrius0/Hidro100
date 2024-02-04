import sys
from PyQt5 import QtWidgets 

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.yazi_alani=QtWidgets.QTextEdit(self)
        self.yazi_alani.setGeometry(10,10,350,400)
        
        #kutucukları ayrı ayrı silme fonksiyonu ve radio butonların tanımları 
        self.radio_yazisi = QtWidgets.QLabel("Which square you want to clear ")
        self.temizle1 = QtWidgets.QRadioButton("",self)
        self.temizle2 = QtWidgets.QRadioButton("",self)
        self.temizle3 = QtWidgets.QRadioButton("",self)
        self.temizle4 = QtWidgets.QRadioButton("",self)

        self.write_place = QtWidgets.QLabel("")
        
        self.buton = QtWidgets.QPushButton("Temizle",self)
        self.buton.move(460,420)

        self.temizle1.move(380,45)
        self.temizle2.move(380,150)
        self.temizle3.move(380,260)
        self.temizle4.move(380,370)
        self.buton.clicked.connect(lambda : self.click())

        self.buton_temizle = QtWidgets.QPushButton("SİLECEĞİNİ SEÇ")
        
        
        
        #Sağ tarafta kaydedilen notların olduğu kısım
        self.kayitli_kutucuk=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk.move(400,10)
        self.kayitli_kutucuk.setGeometry(400,30,200,60)
        
        self.kayitli_kutucuk_2=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_2.setGeometry(400,135,200,60)
        
        self.kayitli_kutucuk_3=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_3.setGeometry(400,240,200,60)
        
        self.kayitli_kutucuk_4=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_4.setGeometry(400,345,200,60)
        #---------------------------------------------------------
        
        
        
        self.buton_kaydet=QtWidgets.QPushButton("Kaydet",self)
        self.buton_kaydet.move(100,420)
        
        
        self.buton_kaydet.clicked.connect(self.kaydet_clicked)

        self.show()
    
        
    def kaydet_clicked(self):
        yazi=self.yazi_alani.toPlainText()

        if not self.kayitli_kutucuk.toPlainText():
            self.kayitli_kutucuk.append(yazi)
            self.yazi_alani.clear()
            self.kayitli_kutucuk.setDisabled(True)
        
        elif not self.kayitli_kutucuk_2.toPlainText():
            self.kayitli_kutucuk_2.append(yazi)
            self.yazi_alani.clear()
            self.kayitli_kutucuk_2.setDisabled(True)
        
        elif not self.kayitli_kutucuk_3.toPlainText():
            self.kayitli_kutucuk_3.append(yazi)
            self.yazi_alani.clear()
            self.kayitli_kutucuk_3.setDisabled(True)
        
        elif not self.kayitli_kutucuk_4.toPlainText():
            self.kayitli_kutucuk_4.append(yazi)
            self.yazi_alani.clear()
            self.kayitli_kutucuk_4.setDisabled(True)
        else:
            pass    

    #Radio butonlarla beraber tanımlanan click fonksiyonunu kutucukların silimine bağlayan kısım    
    def click(self):
        if self.temizle1.isChecked():
            self.kayitli_kutucuk.clear()
        elif self.temizle2.isChecked():
            self.kayitli_kutucuk_2.clear()
        elif self.temizle3.isChecked():
            self.kayitli_kutucuk_3.clear()
        elif self.temizle4.isChecked():
            self.kayitli_kutucuk_4.clear()


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())    

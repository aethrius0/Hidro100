import sys
from PyQt5 import QtWidgets 

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.baslik_1=QtWidgets.QLabel(self)
        self.baslik_2=QtWidgets.QLabel(self)
        self.baslik_3=QtWidgets.QLabel(self)
        self.baslik_4=QtWidgets.QLabel(self)
        self.yazi_alani=QtWidgets.QTextEdit(self)
        self.yazi_alani.setGeometry(10,10,350,400)
        
        #kutucukları ayrı ayrı silme fonksiyonu ve radio butonların tanımları 
        self.sec1 = QtWidgets.QRadioButton("",self)
        self.sec2 = QtWidgets.QRadioButton("",self)
        self.sec3 = QtWidgets.QRadioButton("",self)
        self.sec4 = QtWidgets.QRadioButton("",self)
        
        self.buton_ac=QtWidgets.QPushButton("Aç",self)
        self.buton_temizle = QtWidgets.QPushButton("Temizle",self)
        self.buton_kaydet=QtWidgets.QPushButton("Kaydet",self)
        
        self.buton_temizle.move(500,420)
        self.buton_ac.move(400,420)
        self.sec1.move(380,45)
        self.sec2.move(380,150)
        self.sec3.move(380,260)
        self.sec4.move(380,370)
        self.buton_kaydet.move(150,420)
        self.baslik_1.move(400,10)
        self.baslik_2.move(400,115)
        self.baslik_3.move(400,220)
        self.baslik_4.move(400,325)
        
        self.buton_temizle.clicked.connect(lambda : self.temizle_clicked())
        self.buton_ac.clicked.connect(self.ac_clicked)
        self.buton_kaydet.clicked.connect(self.kaydet_clicked)
        
        
        #Sağ tarafta kaydedilen notların olduğu kısım
        self.kayitli_kutucuk=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk.setGeometry(400,30,200,60)
        
        self.kayitli_kutucuk_2=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_2.setGeometry(400,135,200,60)
        
        self.kayitli_kutucuk_3=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_3.setGeometry(400,240,200,60)
        
        self.kayitli_kutucuk_4=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_4.setGeometry(400,345,200,60)
        #---------------------------------------------------------
        
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
    def temizle_clicked(self):
        if self.sec1.isChecked():
            self.kayitli_kutucuk.clear()
        elif self.sec2.isChecked():
            self.kayitli_kutucuk_2.clear()
        elif self.sec3.isChecked():
            self.kayitli_kutucuk_3.clear()
        elif self.sec4.isChecked():
            self.kayitli_kutucuk_4.clear()

    def ac_clicked(self):
        if self.sec1.isChecked():
            ac_text = self.kayitli_kutucuk.toPlainText()
            self.yazi_alani.setPlainText(ac_text)
        elif self.sec2.isChecked():
            ac_text2 = self.kayitli_kutucuk_2.toPlainText()
            self.yazi_alani.setPlainText(ac_text2)
        elif self.sec3.isChecked():
            ac_text3 = self.kayitli_kutucuk_3.toPlainText()
            self.yazi_alani.setPlainText(ac_text3)
        elif self.sec4.isChecked():
            ac_text4 = self.kayitli_kutucuk_4.toPlainText()
            self.yazi_alani.setPlainText(ac_text4)
            


 


app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())    

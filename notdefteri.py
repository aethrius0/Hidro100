import sys
from PyQt5 import QtWidgets 

# Yusuf Ekledi 2
#aaaaaa
#aaa
#aaaaaaaaa

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        self.setWindowTitle("Not defteri")  #Arayüzün başlığı
        
        self.yazi_alani=QtWidgets.QTextEdit(self)   #Notları aldığımız ana kısım
        self.yazi_alani.setGeometry(10,10,350,400)
        
        
        #Kutucukları ayrı ayrı silme fonksiyonu ve radio butonların tanımları 
        self.sec1 = QtWidgets.QRadioButton("",self)
        self.sec2 = QtWidgets.QRadioButton("",self)
        self.sec3 = QtWidgets.QRadioButton("",self)
        self.sec4 = QtWidgets.QRadioButton("",self)
        
        self.buton_ac=QtWidgets.QPushButton("Aç",self)
        self.buton_temizle = QtWidgets.QPushButton("Temizle",self)
        self.buton_kaydet=QtWidgets.QPushButton("Kaydet",self)
        
        self.buton_temizle.move(500,420)    #Buton ve radio butonlarının yerleri
        self.buton_ac.move(400,420)
        self.sec1.move(380,45)
        self.sec2.move(380,150)
        self.sec3.move(380,260)
        self.sec4.move(380,370)
        self.buton_kaydet.move(150,420)
        
        
        self.buton_temizle.clicked.connect(lambda : self.temizle_clicked())    #Butonların bağlanma noktaları
        self.buton_ac.clicked.connect(self.ac_clicked)
        self.buton_kaydet.clicked.connect(self.kaydet_clicked)
        
        
        #Sağ tarafta kaydedilen notların olduğu kısım-----
        self.kayitli_kutucuk=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk.setGeometry(400,30,200,60)
        
        self.kayitli_kutucuk_2=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_2.setGeometry(400,135,200,60)
        
        self.kayitli_kutucuk_3=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_3.setGeometry(400,240,200,60)
        
        self.kayitli_kutucuk_4=QtWidgets.QTextEdit(self)
        self.kayitli_kutucuk_4.setGeometry(400,345,200,60)
        
        self.baslik_1=QtWidgets.QLabel(self)  #Sağdaki kayıtlı notların başlıklarının yazılıp yerlerinin belirlendiği kısım
        self.baslik_2=QtWidgets.QLabel(self)
        self.baslik_3=QtWidgets.QLabel(self)
        self.baslik_4=QtWidgets.QLabel(self)
        
        self.baslik_1.setText("Kayıtlı Not-1")
        self.baslik_2.setText("Kayıtlı Not-2")
        self.baslik_3.setText("Kayıtlı Not-3")
        self.baslik_4.setText("Kayıtlı Not-4")
        
        self.baslik_1.move(400,10)
        self.baslik_2.move(400,115)
        self.baslik_3.move(400,220)
        self.baslik_4.move(400,325)
        #---------------------------------------------------------
        
        self.show()
    
        
    def kaydet_clicked(self):   #Kaydet butonuna tıkladığımızda notu kayıtlı notlara kaydeden fonksiyonun komut satırı
        yazi=self.yazi_alani.toPlainText()

        if not self.kayitli_kutucuk.toPlainText():
            self.kayitli_kutucuk.append(yazi)        #Yazıyı kayıtlı kutucuklara yerleştiren kod satırı
            self.yazi_alani.clear()                  #Yazıyı kaydettikten sonra ana kısmın tekrardan boş kalmasını sağlayan kod satırı
            self.kayitli_kutucuk.setDisabled(True)   #Kayıtlı kutucuğun hiçbir şekilde değiştirilemez olmasını sağlayan kod satırı
        
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

       
    def temizle_clicked(self):     #Radio butonlarla beraber tanımlanan click fonksiyonunu kutucukların silimine bağlayan kısım 
        if self.sec1.isChecked():
            self.kayitli_kutucuk.clear()
        elif self.sec2.isChecked():
            self.kayitli_kutucuk_2.clear()
        elif self.sec3.isChecked():
            self.kayitli_kutucuk_3.clear()
        elif self.sec4.isChecked():
            self.kayitli_kutucuk_4.clear()

    def ac_clicked(self):   #Aç butonuna tıkladığımızda notu ana ekrana yazdıran fonksiyonun komut satırı
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

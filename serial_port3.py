from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
import sys
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort


class Window(QMainWindow):
    
    class CircularBuffer:
        def __init__(self,size):
            self.size=size
            self.buffer=[None]* size
            self.head = 0
            self.tail = 0
            self.full = False

        def add(self,item):
            self.buffer[self.head]= item
            self.head = (self.head + 1) % self.size
            if self.head == self.tail:
                self.tail=(self.tail + 1) % self.size
                self.full= True
        
        def get(self):
            if not self.full:
                return None
            
            item= self.buffer[self.tail]
            self.tail= (self.tail + 1) % self.size
            self.full = self.head != self.tail
            return item

    def __init__(self):
        super().__init__()
        self.serialPort = QSerialPort()
        self.buffer = self.CircularBuffer(3)
        self.initUI()
        self.listSerialports()

    #seri portları listeler
    def listSerialports(self):
        serialPortInfo = QSerialPortInfo()
        for serialPort in serialPortInfo.availablePorts():
            self.comboSerialportList.addItem(serialPort.portName())

    # seri porttan veri gönderir
    def portSendData(self):
        self.serialPort.write(self.lineEditSendData.text().encode())

    def portConnect(self):
        # haberleşmek için aynı olması gereken özellikler
        self.serialPort.setPortName(self.comboSerialportList.currentText())
        self.serialPort.setBaudRate(QSerialPort.Baud9600)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setParity(QSerialPort.EvenParity)
        self.serialPort.setStopBits(QSerialPort.OneStop)

        # bağlıysa bidaha bağlanmasın diye kontrol ediyoruz
        if not self.serialPort.isOpen():
            self.serialPort.open(QSerialPort.ReadWrite)
            #başta silik görünmesi için
            self.pushButtonConnect.setEnabled(False)
            self.pushButtonDisconnect.setEnabled(True)
            self.pushButtonSend.setEnabled(True)

    def portDisconnect(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            self.pushButtonConnect.setEnabled(True)
            self.pushButtonDisconnect.setEnabled(False)
            self.pushButtonSend.setEnabled(False)

    def portDataReceived(self):
        # seri porttan gelen veriyi okur
        data = self.serialPort.readAll()
        self.buffer.add(data.data())
        
        #buffer doluysa veriyi işle
        if self.buffer.full:
            #veri depolamak için array
            received_data = bytearray()
            
            while self.buffer.full:
                received_data += self.buffer.get()
            
            # veriyi string olarak çözelim
            data_int = received_data.decode()

            # veriyi ekrana gönderir
            self.textEditReceiveData.append(data_int)

        

    def initUI(self):

        # pencerenin boyutu ve düzeni ayarlanıyo
        self.setGeometry(20, 50, 300, 200)
        self.setWindowTitle("serial port 2")
        vboxmain = QVBoxLayout()
        hbox1 = QHBoxLayout()
        self.comboSerialportList = QComboBox()

        hbox1.addWidget(self.comboSerialportList)
        # butonlar oluşturuldu
        self.pushButtonConnect = QPushButton("bağlan")
        self.pushButtonDisconnect = QPushButton("bağlantıyı kes")
        self.pushButtonDisconnect.setEnabled(False)

        hbox1.addWidget(self.pushButtonConnect)
        hbox1.addWidget(self.pushButtonDisconnect)
        hbox1.addStretch()
        vboxmain.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        #gelen mesaj kutusu
        self.textEditReceiveData = QTextEdit()
        self.textEditReceiveData.setFixedSize(300, 100)
        hbox2.addWidget(self.textEditReceiveData)
        vboxmain.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        #gönder kutusu
        self.lineEditSendData = QLineEdit()
        self.pushButtonSend = QPushButton("gönder")
        self.pushButtonSend.setEnabled(False)
        hbox3.addWidget(self.lineEditSendData)
        hbox3.addWidget(self.pushButtonSend)
        vboxmain.addLayout(hbox3)

        vboxmain.addStretch()
        centralWidget = QWidget()
        centralWidget.setLayout(vboxmain)
        self.setCentralWidget(centralWidget)

        #butonları fonksiyonlara bağlıyo
        self.pushButtonConnect.clicked.connect(self.portConnect)
        self.pushButtonDisconnect.clicked.connect(self.portDisconnect)
        self.pushButtonSend.clicked.connect(self.portSendData)
        self.serialPort.readyRead.connect(self.portDataReceived)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

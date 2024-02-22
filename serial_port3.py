from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
import sys
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.serialPort = QSerialPort()
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
        self.textEditReceiveData.append(self.serialPort.readAll().data().decode())

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

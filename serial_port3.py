import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort


class SerialCommunication:
    
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
            self.full= self.head == self.tail
        
        def get(self):
            if not self.full:
                return None
            
            item= self.buffer[self.tail]
            self.tail= (self.tail + 1) % self.size
            self.full = self.head != self.tail
            return item

    def __init__(self):
        
        self.serialPort = QSerialPort()
        self.buffer = self.CircularBuffer(8)
        self.serialPort.readyRead.connect(self.portDataReceived)

    #seri portları listeler
    def listSerialports(self):
        serialPortInfo = QSerialPortInfo()
        serial_ports = [port.portName() for port in serialPortInfo.availablePorts()]
        return serial_ports

    # seri porttan veri gönderir
    def portSendData(self,data):
        self.serialPort.write(data.encode())

    def portConnect(self, port_name):
        # haberleşmek için aynı olması gereken özellikler
        self.serialPort.setPortName(port_name)
        self.serialPort.setBaudRate(QSerialPort.Baud9600)
        self.serialPort.setDataBits(QSerialPort.Data8)
        self.serialPort.setParity(QSerialPort.EvenParity)
        self.serialPort.setStopBits(QSerialPort.OneStop)

        # bağlıysa bidaha bağlanmasın diye kontrol ediyoruz
        if not self.serialPort.isOpen():
            self.serialPort.open(QSerialPort.ReadWrite)
    

    def portDisconnect(self):
        if self.serialPort.isOpen():
            self.serialPort.close()

    def portDataReceived(self):
        # seri porttan gelen veriyi okur
        bytes_available = self.serialPort.bytesAvailable()
        
        if bytes_available > 0:
            data = self.serialPort.read(bytes_available)
            self.buffer.add(data)
            #buffer doluysa veriyi işle
            if self.buffer.full:
                #veri depolamak için array
                received_data = bytearray()
                
                while self.buffer.full:
                    received_data += self.buffer.get()
                
                while len(received_data) >= 8:
                    packet = received_data[:8]   
                    received_data = received_data[8:] 
                    packet_str = packet.decode()  
                    print(packet_str)
                

if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    serial_communication = SerialCommunication()   
    #seri portları listeler
    serial_ports = serial_communication.listSerialports()
    print("Available serial ports:", serial_ports)

    if serial_ports:
        selected_port = input("Enter the port name to connect: ")
        serial_communication.portConnect(selected_port)
        print(f"Connected to port: {selected_port}")

        while True:
            command = input("Enter data to send (or 'exit' to quit): ")
            if command.lower() == "exit":
                break
            serial_communication.portSendData(command)

        serial_communication.portDisconnect()
        print("Disconnected from port.")

    else:
        print("No serial ports available.")

    sys.exit(app.exec())

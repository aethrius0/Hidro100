import sys
import random
from PyQt5.QtCore import QObject, QUrl, QTimer, QVariantAnimation, QThread, pyqtSignal
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QThread, pyqtSignal
import veri_isleme
import serial_port3
import serial
import time


class WorkerThread(QThread):
    thread_signal = pyqtSignal(bytes)

    def run(self):
        self.GetValuesSelin()

    def GetValuesSelin(self):
        while True:
            data = serial_port3.get_packet(ser, circular_buffer, 128)
            # print(data)
            self.thread_signal.emit(data)


class Speedometer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view=None
        
        
        self.timer_speed = QTimer(self)
        self.timer_battery = QTimer(self)
        self.timer_temp = QTimer(self)
        self.timer_watt = QTimer(self)
        self.timer_volt = QTimer(self)
        self.timer_updateTextField = QTimer(self)
        # self.GetValues = QTimer(self)

        self.timer_speed.timeout.connect(self.updateValueSpeed)
        self.timer_battery.timeout.connect(self.updateValueBattery)
        self.timer_temp.timeout.connect(self.updateValueTemp)
        self.timer_watt.timeout.connect(self.updateValueWatt)
        self.timer_volt.timeout.connect(self.updateValueVolt)
        self.timer_updateTextField.timeout.connect(self.updateTextFieldValues)
        # self.GetValues.timeout.connect(self.GetValuesSelin)

        self.timer_speed.start(1000)
        self.timer_battery.start(1000)
        self.timer_temp.start(1000)
        self.timer_watt.start(1000)
        self.timer_volt.start(1000)
        self.timer_updateTextField.start(1000)
        # self.GetValues.start(1000)
        

        self.current_speed = 0
        self.current_battery = 0
        self.current_temp = 0
        self.current_watt = 0
        self.current_volt = 0 

        self.__data = None
        self.data_thread = WorkerThread()
        self.data_thread.thread_signal.connect(self.data_thread_handler)


        
    def data_thread_handler(self, data):
        print(f"DATA IS: {data}")
        self.__data = data


    def start_thread(self):
        self.data_thread.start()
        
    def GetValuesSelin(self):
        
        self.__data = serial_port3.get_packet(ser, circular_buffer, 128)
        print(self.__data)


    def updateTextFieldValues(self):
        
        if self.view:
            
            textField1 = self.view.findChild(QObject, "textField1")
            
            textField2 = self.view.findChild(QObject, "textField2")
            
            textField3 = self.view.findChild(QObject, "textField3")
            
            textField4 = self.view.findChild(QObject, "textField4")
            
            textField5 = self.view.findChild(QObject, "textField5")
            
            textField6 = self.view.findChild(QObject, "textField6")
            
            textField7 = self.view.findChild(QObject, "textField7")
            
            textField8 = self.view.findChild(QObject, "textField8")
            
            textField9 = self.view.findChild(QObject, "textField9")
            
            textField10 = self.view.findChild(QObject, "textField10")
            
            textField11 = self.view.findChild(QObject, "textField11")
            
            textField12 = self.view.findChild(QObject, "textField12")
            
            textField13 = self.view.findChild(QObject, "textField13")
            
            textField14 = self.view.findChild(QObject, "textField14")
            
            textField15 = self.view.findChild(QObject, "textField15")
            
            
            textFieldSpeed= self.view.findChild(QObject,"textFieldSpeed")
            
            
         
            
            
            
            if textField1:
                value = random.randint(0, 100)
                textField1.setProperty("text", value)
                
            if textField2:
                value = random.randint(0, 100)
                textField2.setProperty("text", value)
                
            if textField3:
                value = random.randint(0, 100)
                textField3.setProperty("text", value)
                
            if textField4:
                value = random.randint(0, 100)
                textField4.setProperty("text", value)
                
            if textField5:
                value = random.randint(0, 100)
                textField5.setProperty("text", value)
                
            if textField6:
                value = random.randint(0, 100)
                textField6.setProperty("text", value)
                
            if textField7:
                value = random.randint(0, 100)
                textField7.setProperty("text", value)
                
            if textField8:
                value = random.randint(0, 100)
                textField8.setProperty("text", value)
                
            if textField9:
                value = random.randint(0, 100)
                textField9.setProperty("text", value)
                
            if textField10:
                value = random.randint(0, 100)
                textField10.setProperty("text", value)
                
            if textField11:
                value = random.randint(0, 100)
                textField11.setProperty("text", value)
                
            if textField12:
                value = random.randint(0, 100)
                textField12.setProperty("text", value)
                
            if textField13:
                value = random.randint(0, 100)
                textField13.setProperty("text", value)
                
            if textField14:
                value = random.randint(0, 100)
                textField14.setProperty("text", value)
                
            if textField15:
                value = random.randint(0, 100)
                textField15.setProperty("text", value)
            
             
            if textFieldSpeed:
                speed_text = str(self.current_speed) + " km/h"
                textFieldSpeed.setProperty("text", speed_text)  
            
        
        

    
    def updateValueSpeed(self):
        #print(f"DATA IS: {self.__data}")
        if self.__data is not None:
            self.target_speed = float((veri_isleme.Speed(self.__data))[0])
            self.anim_speed = QVariantAnimation()
            self.anim_speed.setStartValue(self.current_speed)
            self.anim_speed.setEndValue(self.target_speed)
            self.anim_speed.setDuration(1000)
            self.anim_speed.valueChanged.connect(self.setSpeed)
            self.anim_speed.start()
            self.current_speed = self.target_speed
        
            
            
            
        
        
        

    def updateValueBattery(self):
        if self.__data is not None:
            self.target_battery = float((veri_isleme.State_of_charge(self.__data))[0])
            self.anim_battery = QVariantAnimation()
            self.anim_battery.setStartValue(self.current_battery)
            self.anim_battery.setEndValue(self.target_battery)
            self.anim_battery.setDuration(1000)
            self.anim_battery.valueChanged.connect(self.setBattery)
            self.anim_battery.start()
            self.current_battery = self.target_battery

    def updateValueTemp(self):
        if self.__data is not None:
            self.target_temp = float((veri_isleme.temperature(self.__data))[0])
            self.anim_temp = QVariantAnimation()
            self.anim_temp.setStartValue(self.current_temp)
            self.anim_temp.setEndValue(self.target_temp)
            self.anim_temp.setDuration(1000)
            self.anim_temp.valueChanged.connect(self.setTemp)
            self.anim_temp.start()
            self.current_temp = self.target_temp

    def updateValueWatt(self):
        if self.__data is not None:
            self.target_watt = float((veri_isleme.Wh(self.__data))[0])
            self.anim_watt = QVariantAnimation()
            self.anim_watt.setStartValue(self.current_watt)
            self.anim_watt.setEndValue(self.target_watt)
            self.anim_watt.setDuration(1000)
            self.anim_watt.valueChanged.connect(self.setWatt)
            self.anim_watt.start()
            self.current_watt = self.target_watt

    def updateValueVolt(self):
        if self.__data  is not None:
            self.target_volt = float((veri_isleme.volt_general(self.__data))[0])
            self.anim_volt = QVariantAnimation()
            self.anim_volt.setStartValue(self.current_volt)
            self.anim_volt.setEndValue(self.target_volt)
            self.anim_volt.setDuration(1000)
            self.anim_volt.valueChanged.connect(self.setVolt)
            self.anim_volt.start()
            self.current_volt = self.target_volt

    def setSpeed(self, value):      
        gauge.setProperty('speedgauge_value', value)
      
    def setBattery(self, value):
        gauge2.setProperty('whgauge_value', value)

    def setTemp(self, value):
        gauge3.setProperty('tempgauge_value', value)

    def setWatt(self, value):
        gauge4.setProperty('voltgauge_value', value)

    def setVolt(self, value):
        gauge5.setProperty('btgauge_value', value)
    


class SpeedometerApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.view = QQuickView()
        self.view.setTitle("Vehicle Panel")
        self.view.setSource(QUrl('speedometer.qml'))
        self.speedometer = Speedometer()
        self.speedometer.start_thread()
        
        if self.speedometer:
            self.speedometer.view = self.view  # Speedometer sınıfına view özelliğini atama
            self.speedometer.updateTextFieldValues()
        
        
        

    def run(self):
        
        global gauge, gauge2, gauge3, gauge4, gauge5
        gauge = self.view.findChild(QObject, 'speed_gauge')
        gauge2 = self.view.findChild(QObject, 'wh_gauge')
        gauge3 = self.view.findChild(QObject, 'temp_gauge')
        gauge4 = self.view.findChild(QObject, 'volt_gauge')
        gauge5 = self.view.findChild(QObject, 'bt_gauge')
        

        self.view.show()
        return self.exec_()



if __name__ == "__main__":
    global ser, circular_buffer
    # Seri port bağlantısını oluştur
    ser = serial.Serial("COM15", 9600)
    # istenilen boyutta bir döngüsel tampon oluştur
    circular_buffer = serial_port3.CircularBuffer(128)

    app = SpeedometerApp(sys.argv) 
    sys.exit(app.run())
        

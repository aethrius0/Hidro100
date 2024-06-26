import sys
import os
import random
from PyQt5.QtCore import QObject, QUrl, QTimer, QVariantAnimation, QThread, pyqtSignal
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout,QWidget
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine,qmlRegisterType
from PyQt5.QtCore import QThread,pyqtSlot,pyqtSignal
import veri_isleme
import serial_port3
import serial
import time



class WorkerThread(QThread):
    thread_signal = pyqtSignal(bytes)

    def run(self):
        self.GetValuesPorts()

    def GetValuesPorts(self):
        while True:
            data = serial_port3.get_packet(ser, circular_buffer, 128)
            # print(data)
            self.thread_signal.emit(data)
            


        
class Speedometer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view=None
        self.current_time = time.strftime("%H:%M:%S")
        self.current_date_time = time.strftime("%Y-%m-%d")
         
        
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
        # self.GetValues.timeout.connect(self.GetValuesPorts)

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
        
        
        

        self.clear_log_file()
        
    
        
        
    
    
        
    def data_thread_handler(self, data):
        

        with open("log.txt", "a") as log_file:
            self.current_time = time.strftime("%H:%M:%S")
            self.current_date_time = time.strftime("%Y-%m-%d")

            speed = float(veri_isleme.Speed(data)[0])
            temp = float(veri_isleme.temperature(data)[0])
            volt = float(veri_isleme.volt_general(data)[0])
            wh = float(veri_isleme.Wh(data)[0])
            soc = float(veri_isleme.State_of_charge(data)[0])

            print(f"{self.current_date_time:12}{self.current_time:8} {speed:6.1f} {temp:6.2f} {volt:6.2f} "
                  f"{wh:6.1f} {soc:6.2f}", file=log_file)

        self.__data = data

    def clear_log_file(self):
        with open("log.txt", "w") as log_file:
            print(f"{'DATE':11} {'TIME':10} {'Kph':6} {'TEMP':6} {'VOLT':6} {'Wh':6} {'SoC':6}", file=log_file)
        
        
        
        

    def start_thread(self):
        self.data_thread.start()
        
    def GetValuesPorts(self):
        
        self.__data = serial_port3.get_packet(ser, circular_buffer, 128)
        
        
    
            


    def updateTextFieldValues(self):
        if self.__data is None:
            return  # Veriler henüz alınmadıysa hiçbir şey yapma
        
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
            
            textFieldWh =self.view.findChild(QObject,"textFieldWh")
            
            textFieldVolt =self.view.findChild(QObject,"textFieldVolt")
            
            textFieldTemp =self.view.findChild(QObject,"textFieldTemp")
            
            textFieldBt =self.view.findChild(QObject,"textFieldBt")
            
            
            
            
            textInput = self.view.findChild(QObject, "textInput")
            
         
            
            
            
            if textField1:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField1.setProperty("text", str(value) + " V")
                
            if textField2:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField2.setProperty("text", str(value) + " V")
                
            if textField3:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField3.setProperty("text", str(value) + " V")
                
            if textField4:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField4.setProperty("text", str(value) + " V")
                
            if textField5:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField5.setProperty("text", str(value) + " V")
                
            if textField6:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField6.setProperty("text", str(value) + " V")
                
            if textField7:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField7.setProperty("text", str(value) + " V")
                
            if textField8:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField8.setProperty("text", str(value) + " V")
                
            if textField9:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField9.setProperty("text", str(value) + " V")
                
            if textField10:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField10.setProperty("text", str(value) + " V")
                
            if textField11:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField11.setProperty("text", str(value) + " V")
                
            if textField12:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField12.setProperty("text", str(value) + " V")
                
            if textField13:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField13.setProperty("text", str(value) + " V")
                
            if textField14:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField14.setProperty("text", str(value) + " V")
                
            if textField15:
                value = float(veri_isleme.volts_cells(self.__data)[0])
                textField15.setProperty("text", str(value) + " V")
            
             
            #if textFieldSpeed:
            #    if self.current_speed == 0:  # Eğer batarya seviyesi 0 ise
            #        speed_text = "N/A km/h"
            #        textFieldSpeed.setProperty("text", speed_text)
            #    else:
            #        speed_text = str(self.current_speed) + " km/h"
            #    textFieldSpeed.setProperty("text", speed_text) 
                
            if textFieldWh:
                if self.current_watt == 0:  # Eğer batarya seviyesi 0 ise
                    watt_text = "N/A Wh"
                    textFieldWh.setProperty("text", watt_text)
                else:
                    watt_text = str(self.current_watt) + " Wh"
                textFieldWh.setProperty("text", watt_text) 
                
            if textFieldVolt:
                if self.current_volt == 0:  # Eğer batarya seviyesi 0 ise
                    volt_text = "N/A V"
                    textFieldVolt.setProperty("text", volt_text)
                else:
                    volt_text = str(self.current_volt) + " V"
                textFieldVolt.setProperty("text", volt_text)
                
            if textFieldTemp:
                if self.current_temp == 0:  # Eğer batarya seviyesi 0 ise
                    temp_text = "N/A °C"
                    textFieldTemp.setProperty("text", temp_text)
                else:
                    temp_text = str(self.current_temp) + " °C"
                textFieldTemp.setProperty("text", temp_text)
               
            if textFieldBt:
                if self.current_battery == 0:  # Eğer batarya seviyesi 0 ise
                    bt_text = "  N/A %"
                    textFieldBt.setProperty("text", bt_text)
                else:
                    bt_text = str(self.current_battery) + " %"
                textFieldBt.setProperty("text", bt_text)

            
        
            
            if self.view:
                textInput = self.view.findChild(QObject, "textInput")
                if textInput:
                    new_text = "WORKING PROPERLY..."
                    textInput.setProperty("text", new_text)
                    if self.current_temp>70:
                        new_text="WARNING!! HIGH TEMPERATURE !!"
                        textInput.setProperty("text", new_text)
                        
                    elif self.current_temp<3:
                        new_text="WARNING!! LOW TEMPERATURE !!"
                        textInput.setProperty("text", new_text)
                        
                    elif self.current_volt>20:
                        new_text="WARNING!! HIGH VOLTAGE !!"
                        textInput.setProperty("text", new_text)
                    
                    elif self.current_volt<3:
                        new_text="WARNING!! LOW VOLTAGE !!"
                        textInput.setProperty("text", new_text)
                    
                    elif self.current_battery<20:
                        new_text="WARNING!! LOW BATTERY CHARGE !!"
                        textInput.setProperty("text", new_text)
                    
                    
                        
                    
                        
                else:
                    print("textInput bulunamadı.")
        

    
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
      
    def setWatt(self, value):
        gauge2.setProperty('whgauge_value', value)

    def setTemp(self, value):
        gauge3.setProperty('tempgauge_value', value)

    def setVolt(self, value):
        gauge4.setProperty('voltgauge_value', value)

    def setBattery(self, value):
        gauge6.setProperty('btgauge_value', value)
    


class SpeedometerApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.view = QQuickView()
        self.view.setTitle("HIDROKET VEHICLE PANEL")
        self.view.setSource(QUrl('speedometer.qml'))
        
        self.speedometer = Speedometer()
        self.speedometer.start_thread()
        
       
        
        if self.speedometer:
            self.speedometer.view = self.view  # Speedometer sınıfına view özelliğini atama
            self.speedometer.updateTextFieldValues()
            
 

    def run(self):
        
        global gauge, gauge2, gauge3, gauge4 ,gauge6
        gauge = self.view.findChild(QObject, 'speed_gauge')
        gauge2 = self.view.findChild(QObject, 'wh_gauge')
        gauge3 = self.view.findChild(QObject, 'temp_gauge')
        gauge4 = self.view.findChild(QObject, 'volt_gauge')
        #gauge5 = self.view.findChild(QObject, 'bt_gauge')
        gauge6 = self.view.findChild(QObject, "bt_gauge")
        
        
        
        
        self.view.show()
        return self.exec_()
    
    
 


if __name__ == "__main__":
    global ser, circular_buffer
    # Seri port bağlantısını oluştur
    ser = serial.Serial("COM9", 9600)
    # istenilen boyutta bir döngüsel tampon oluştur
    circular_buffer = serial_port3.CircularBuffer(128)  

    app = SpeedometerApp(sys.argv) 
    sys.exit(app.run())
        

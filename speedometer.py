import sys
import random
from PyQt5.QtCore import QObject, QUrl, QTimer, QVariantAnimation, QThread, pyqtSignal
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine

class Speedometer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        
        
        self.timer_speed = QTimer(self)
        self.timer_battery = QTimer(self)
        self.timer_temp = QTimer(self)
        self.timer_watt = QTimer(self)
        self.timer_volt = QTimer(self)
        self.updateValuesTimer = QTimer(self)

        self.timer_speed.timeout.connect(self.updateValueSpeed)
        self.timer_battery.timeout.connect(self.updateValueBattery)
        self.timer_temp.timeout.connect(self.updateValueTemp)
        self.timer_watt.timeout.connect(self.updateValueWatt)
        self.timer_volt.timeout.connect(self.updateValueVolt)
        self.updateValuesTimer.timeout.connect(self.updateTextFieldValues)

        self.timer_speed.start(1000)
        self.timer_battery.start(1000)
        self.timer_temp.start(1000)
        self.timer_watt.start(1000)
        self.timer_volt.start(1000)
        self.updateValuesTimer.start(1000)  # Her 1 saniyede bir güncelle

        self.current_speed = 0
        self.current_battery = 0
        self.current_temp = 0
        self.current_watt = 0
        self.current_volt = 0

    def updateTextFieldValues(self):
        # QML'deki tüm TextField'lara rastgele değer atama
        for i in range(1, 16):  # 15 TextField var
            textFieldName = f"textField{i}"
            textField = self.view.rootObject().findChild(QObject, textFieldName)
            if textField:
                randomValue = str(random.randint(0, 100))  # Rastgele bir değer üret
                textField.setProperty("text", randomValue)

    
    def updateValueSpeed(self):
        self.target_speed = random.randint(0, 70)
        self.anim_speed = QVariantAnimation()
        self.anim_speed.setStartValue(self.current_speed)
        self.anim_speed.setEndValue(self.target_speed)
        self.anim_speed.setDuration(1000)
        self.anim_speed.valueChanged.connect(self.setSpeed)
        self.anim_speed.start()
        self.current_speed = self.target_speed

    def updateValueBattery(self):
        self.target_battery = random.randint(0, 100)
        self.anim_battery = QVariantAnimation()
        self.anim_battery.setStartValue(self.current_battery)
        self.anim_battery.setEndValue(self.target_battery)
        self.anim_battery.setDuration(1000)
        self.anim_battery.valueChanged.connect(self.setBattery)
        self.anim_battery.start()
        self.current_battery = self.target_battery

    def updateValueTemp(self):
        self.target_temp = random.randint(0, 100)
        self.anim_temp = QVariantAnimation()
        self.anim_temp.setStartValue(self.current_temp)
        self.anim_temp.setEndValue(self.target_temp)
        self.anim_temp.setDuration(1000)
        self.anim_temp.valueChanged.connect(self.setTemp)
        self.anim_temp.start()
        self.current_temp = self.target_temp

    def updateValueWatt(self):
        self.target_watt = random.randint(0, 24)
        self.anim_watt = QVariantAnimation()
        self.anim_watt.setStartValue(self.current_watt)
        self.anim_watt.setEndValue(self.target_watt)
        self.anim_watt.setDuration(1000)
        self.anim_watt.valueChanged.connect(self.setWatt)
        self.anim_watt.start()
        self.current_watt = self.target_watt

    def updateValueVolt(self):
        self.target_volt = random.randint(0, 100)
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
        self.view.setSource(QUrl('speedometer.qml'))
        self.speedometer = Speedometer()
        self.speedometer.view = self.view

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
    app = SpeedometerApp(sys.argv)
    
    sys.exit(app.run())
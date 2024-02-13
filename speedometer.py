import sys
import time
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlEngine, QQmlComponent
from PyQt5 import QtCore, QtGui
from PyQt5.QtQuick import QQuickView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QQuickView()
    view.setSource(QUrl('speedometer.qml'))
    gauge=view.findChild(QObject,'speed_gauge')
    gauge2=view.findChild(QObject,'wh_gauge')
    gauge3=view.findChild(QObject,'temp_gauge')
    gauge4=view.findChild(QObject,'volt_gauge')
    gauge5=view.findChild(QObject,'bt_gauge')
    gauge.setProperty('speedgauge_value',0)
    gauge2.setProperty('whgauge_value',0)
    gauge3.setProperty('tempgauge_value',0)
    gauge4.setProperty('voltgauge_value',0)
    gauge5.setProperty('btgauge_value',0)
    view.show()
    sys.exit(app.exec_())

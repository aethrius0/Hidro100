import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0

Rectangle {
     width: 1050
     height: 560
     color: "#000000"

     
    Image {
        source: "hidroket-logo.png" 
        anchors.fill: parent 
        opacity: 0.17
        
     }

     Row {

          spacing: 10
          anchors {
               //top: speed_gauge.bottom // Ana bileşenin altından başlasın
               bottom: parent.bottom // Ana bileşenin alt kısmına hizalama
               horizontalCenter: parent.horizontalCenter // Yatay olarak merkezleme
          }

          // 15 kutucuk oluşturma
          Repeater {
               model: 15
               Rectangle {
                    width: 50
                    height: 30
                    border.color: "blue" // Çerçeve rengi
                    border.width: 2 // Çerçeve kalınlığı
                    color: "transparent" // İçi boş kutucuk
                    // Diğer özelliklerini buraya ekleyebilirsiniz
               }
          }
     }
    
    
     CircularGauge {
          objectName: "speed_gauge"
          property real speedgauge_value: 0
          width:400 // göstergenin büyüklük kare olcak
          height:400
          //anchors.centerIn: parent
          x:60   //hız göstergesinin koordinatları
          y:60
          value: speedgauge_value
          maximumValue: 70.0  // Largest Value
          minimumValue: 0.0       // Smallest Value
          style: CircularGaugeStyle {
          id: style
          tickmarkStepSize: 5.0 // Tick Marks

               tickmark: Rectangle {
                    visible: styleData.value < 8000 || styleData.value % 1000 == 0
                    implicitWidth: outerRadius * 0.02
                    antialiasing: true
                    implicitHeight: outerRadius * 0.1
                    color: styleData.value >= 8000 ? "#ffffff" : "#ffffff"
               }

               minorTickmark: Rectangle {
                    visible: styleData.value < 8000
                    implicitWidth: outerRadius * 0.01
                    antialiasing: true
                    implicitHeight: outerRadius * 0.03
                    color: "#0000FF"
               }

               tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color: styleData.value >= 8000 ? "#ffffff" : "#ffffff"
                    antialiasing: true
               }

               needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 0.9
                    antialiasing: true
                    color: "#ff0000"
               }

               foreground: Item {
                    Rectangle {
                         width: outerRadius * 0.1
                         height: width
                         radius: width / 2
                         color: "#b2b2b2"
                         anchors.centerIn: parent
                    }
               }
          }
     }

    
     // İkinci CircularGauge bileşeni
     CircularGauge {
          objectName: "wh_gauge"
          property real whgauge_value: 0
          width:210
          height:210
          x:520
          y:10
          value: whgauge_value
          maximumValue: 100.0  // Largest Value
          minimumValue: 0.0       // Smallest Value
          style: CircularGaugeStyle {
               id: style2
               tickmarkStepSize: 10.0 // Tick Marks

               tickmark: Rectangle {
                    visible: styleData.value < 5000 || styleData.value % 1000 == 0
                    implicitWidth: outerRadius * 0.02
                    antialiasing: true
                    implicitHeight: outerRadius * 0.1
                    color: "#ffffff"
               }

               minorTickmark: Rectangle {
                    visible: styleData.value < 5000
                    implicitWidth: outerRadius * 0.1
                    antialiasing: true
                    implicitHeight: outerRadius * 0.01
                    color: "#0000FF"
               }

               tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color:"#ffffff"
                    antialiasing: true
               }

               needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 0.9
                    antialiasing: true
                    color: "#ff0000"
               }

               foreground: Item {
                    Rectangle {
                         width: outerRadius * 0.1
                         height: width
                         radius: width / 2
                         color: "#b2b2b2"
                         anchors.centerIn: parent
                    }
               }
          }
     }
     
     CircularGauge {
          objectName: "temp_gauge"
          width: 210
          height: 210
          property real tempgauge_value: 0
          x: 800
          y: 10
          value: tempgauge_value
          maximumValue: 100.0  // Largest Value
          minimumValue: 0.0       // Smallest Value
          style: CircularGaugeStyle {
               id: style
               tickmarkStepSize: 10.0 // Tick Marks

               tickmark: Rectangle {
                    visible: styleData.value < 8000 || styleData.value % 1000 == 0
                    implicitWidth: outerRadius * 0.02
                    antialiasing: true
                    implicitHeight: outerRadius * 0.1
                    color: "#ffffff"
               }

               minorTickmark: Rectangle {
                    visible: styleData.value < 8000
                    implicitWidth: outerRadius * 0.1
                    antialiasing: true
                    implicitHeight: outerRadius * 0.01
                    color: "#0000FF"
               }

               tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color: "#ffffff"
                    antialiasing: true
               }

               needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 0.9
                    antialiasing: true
                    color: "#ff0000"
               }

               foreground: Item {
                    Rectangle {
                         width: outerRadius * 0.1
                         height: width
                         radius: width / 2
                         color: "#b2b2b2"
                         anchors.centerIn: parent
                    }
               }
          }
     }
    
     //Voltmeter gauge
     //
     CircularGauge {
            objectName: "volt_gauge"
            property real voltgauge_value: 50  //
            width:210 // göstergenin büyüklük kare olcak
            height:210
            //anchors.centerIn: parent
            x:520   //hız göstergesinin koordinatları
            y:250
            value: voltgauge_value
            maximumValue: 24.0  // Largest Value
            minimumValue: 0.0       // Smallest Value
            style: CircularGaugeStyle {
                id: style
                tickmarkStepSize: 2.0 // Tick Marks

                tickmark: Rectangle {
                    visible: styleData.value < 8000 || styleData.value % 1000 == 0
                    implicitWidth: outerRadius * 0.02
                    antialiasing: true
                    implicitHeight: outerRadius * 0.1
                    color: styleData.value >= 8000 ? "#ADD8E6" : "#ADD8E6"
                }

               minorTickmark: Rectangle {
                    visible: styleData.value < 8000
                    implicitWidth: outerRadius * 0.1
                    antialiasing: true
                    implicitHeight: outerRadius * 0.01
                    color: "#0000FF"
               }

               tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color: styleData.value >= 8000 ? "#ADD8E6" : "#ADD8E6"
                    antialiasing: true
               }

               needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 0.9
                    antialiasing: true
                    color: "#ff0000"
               }





               foreground: Item {
                    Rectangle {
                         width: outerRadius * 0.1
                         height: width
                         radius: width / 2
                         color: "#b2b2b2"
                         anchors.centerIn: parent
                    }
               }
          }
     }

     
     //bt gauge
     CircularGauge {
            objectName: "bt_gauge"
            property real btgauge_value: 50  //
            width:210 // göstergenin büyüklük kare olcak
            height:210
            //anchors.centerIn: parent
            x:800   //hız göstergesinin koordinatları
            y:250
            value: btgauge_value
            maximumValue: 100.0  // Largest Value
            minimumValue: 0.0       // Smallest Value
            style: CircularGaugeStyle {
                id: style
                tickmarkStepSize: 10.0 // Tick Marks

                tickmark: Rectangle {
                    visible: styleData.value < 8000 || styleData.value % 1000 == 0
                    implicitWidth: outerRadius * 0.02
                    antialiasing: true
                    implicitHeight: outerRadius * 0.1
                    color: styleData.value >= 8000 ? "#ADD8E6" : "#ADD8E6"
                }

               minorTickmark: Rectangle {
                    visible: styleData.value < 8000
                    implicitWidth: outerRadius * 0.1
                    antialiasing: true
                    implicitHeight: outerRadius * 0.01
                    color: "#0000FF"
               }

               tickmarkLabel:  Text {
                    font.pixelSize: Math.max(6, outerRadius * 0.1)
                    text: styleData.value
                    color: styleData.value >= 8000 ? "#ADD8E6" : "#ADD8E6"
                    antialiasing: true
               }

               needle: Rectangle {
                    y: outerRadius * 0.15
                    implicitWidth: outerRadius * 0.03
                    implicitHeight: outerRadius * 0.9
                    antialiasing: true
                    color: "#ff0000"
               }





               foreground: Item {
                    Rectangle {
                         width: outerRadius * 0.1
                         height: width
                         radius: width / 2
                         color: "#b2b2b2"
                         anchors.centerIn: parent
                    }
               }
          }
     }
     
}


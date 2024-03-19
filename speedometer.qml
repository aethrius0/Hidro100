import QtQuick 2.12
import QtQuick.Controls 2.12
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
        opacity: 0.3
        
        
     }

     Row {
         
          spacing: 10
          anchors {
               
               //top: speed_gauge.bottom // Ana bileşenin altından başlasın
               bottom: parent.bottom // Ana bileşenin alt kısmına hizalama
               horizontalCenter: parent.horizontalCenter // Yatay olarak merkezleme
          }
         
          

     /* Arayüzün aşağısındaki TextField Kutucukları */

          TextField{
               id: textField1
               text:""
               objectName: "textField1"; 
               width:50; 
               height: 30; 
               font.pixelSize: 14; 
               color: "white"; 
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 1"
                    color: "white"
               }
          }

          TextField{ 
               id: textField2; 
               text: ""
               objectName: "textField2"; 
               width:50; 
               height: 30; 
               font.pixelSize: 14; 
               color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 2"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField3; objectName: "textField3"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 3"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField4; objectName: "textField4"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }    
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 4"
                    color: "white"
               } 
          }
          TextField 
          { 
               id: textField5; objectName: "textField5"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 5"
                    color: "white"
               } 
          }
          TextField 
          { 
               id: textField6; objectName: "textField6"; width:50; height: 30; font.pixelSize: 14; color: "white"; 
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 6"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField7; objectName: "textField7"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 7"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField8; objectName: "textField8"; width:50; height: 30; font.pixelSize: 14; color: "white"; 
               background: Rectangle 
               {
               color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 8"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField9; objectName: "textField9"; width:50; height: 30; font.pixelSize: 14; color: "white"; 
               background: Rectangle {
               color: "transparent"; 
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 9"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField10; objectName: "textField10"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 10"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField11; objectName: "textField11"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 11"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField12; objectName: "textField12"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 12"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField13; objectName: "textField13"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 13"
                    color: "white"
               }
          }
          TextField 
          { 
               id: textField14; objectName: "textField14"; width:50; height: 30; font.pixelSize: 14; color: "white";
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 14"
                    color: "white"
               }
               }
          TextField 
          { 
               id: textField15; objectName: "textField15"; width:50; height: 30; font.pixelSize: 14; color: "white"; 
               background: Rectangle {
                    color: "transparent"; // Arka planı şeffaf yapar
               }
               Text{
                    anchors.top: parent.top
                    anchors.topMargin: -10
                    anchors.right: parent.right
                    anchors.rightMargin: 6
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: "CELL 15"
                    color: "white"
               }
          }

     
          

          
     }
     
    
    
     CircularGauge {
          objectName: "speed_gauge"
          property real speedgauge_value: 0
          width:370 // göstergenin büyüklük kare olcak
          height:370
          //anchors.centerIn: parent
          x:60   //hız göstergesinin koordinatları
          y:20
          value: speedgauge_value
          maximumValue: 70.0  // Largest Value
          minimumValue: 0.0       // Smallest Value
          
          
          // Değerin gösterildiği metin
          Text {
               id:textFieldSpeed
               objectName: "textFieldSpeed"
               
               font.pixelSize: 24 // Yazı boyutu
               color: "white" // Yazı rengi
               anchors.horizontalCenter: parent.horizontalCenter // Yatay hizalama
               anchors.top: parent.bottom // Üst kenarın altına hizalama
               anchors.topMargin: -100 // Üst kenarın altına boşluk bırakma
               
               
          }
                  
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
          Text {
               id:textFieldWh
               objectName: "textFieldWh"
               
               font.pixelSize: 24 // Yazı boyutu
               color: "white" // Yazı rengi
               anchors.horizontalCenter: parent.horizontalCenter // Yatay hizalama
               anchors.top: parent.bottom // Üst kenarın altına hizalama
               anchors.topMargin: -70 // Üst kenarın altına boşluk bırakma
               
               
          }
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
          Text {
               id:textFieldTemp
               objectName: "textFieldTemp"
               
               font.pixelSize: 24 // Yazı boyutu
               color: "white" // Yazı rengi
               anchors.horizontalCenter: parent.horizontalCenter // Yatay hizalama
               anchors.top: parent.bottom // Üst kenarın altına hizalama
               anchors.topMargin: -70 // Üst kenarın altına boşluk bırakma
               
               
          }
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
            property real voltgauge_value: 0  //
            width:210 // göstergenin büyüklük kare olcak
            height:210
            //anchors.centerIn: parent
            x:520   //hız göstergesinin koordinatları
            y:250
            value: voltgauge_value
            maximumValue: 24.0  // Largest Value
            minimumValue: 0.0       // Smallest Value
            Text {
               id:textFieldVolt
               objectName: "textFieldVolt"
               
               font.pixelSize: 24 // Yazı boyutu
               color: "white" // Yazı rengi
               anchors.horizontalCenter: parent.horizontalCenter // Yatay hizalama
               anchors.top: parent.bottom // Üst kenarın altına hizalama
               anchors.topMargin: -70 // Üst kenarın altına boşluk bırakma
               
               
          }
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
            property real btgauge_value: 0  //
            width:210 // göstergenin büyüklük kare olcak
            height:210
            //anchors.centerIn: parent
            x:800   //hız göstergesinin koordinatları
            y:250
            value: btgauge_value
            maximumValue: 100.0  // Largest Value
            minimumValue: 0.0       // Smallest Value
            Text {
               id:textFieldBt
               objectName: "textFieldBt"
               
               font.pixelSize: 24 // Yazı boyutu
               color: "white" // Yazı rengi
               anchors.horizontalCenter: parent.horizontalCenter // Yatay hizalama
               anchors.top: parent.bottom // Üst kenarın altına hizalama
               anchors.topMargin: -70 // Üst kenarın altına boşluk bırakma
               
               
          }
            
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

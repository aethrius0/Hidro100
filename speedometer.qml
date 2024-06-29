import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtQuick.Layouts 1.3

Rectangle
{
     
     width: 1050
     height: 560
     color: "#000000"
     
     
     
         
     
    Image {
        source: "hidroket-logo.png" 
        anchors.fill: parent 
        opacity: 0.6
        
        
     }
     

     Row {  
          //Layout.fillWidth: true
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
               width: 60
               height: 30 // Sabit bir yükseklik değeri 
               font.pixelSize: 13; 
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
               width:61; 
               height: 30; 
               font.pixelSize: 13; 
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
               id: textField3; objectName: "textField3"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField4; objectName: "textField4"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField5; objectName: "textField5"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField6; objectName: "textField6"; width:61; height: 30; font.pixelSize: 13; color: "white"; 
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
               id: textField7; objectName: "textField7"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField8; objectName: "textField8"; width:61; height: 30; font.pixelSize: 13; color: "white"; 
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
               id: textField9; objectName: "textField9"; width:61; height: 30; font.pixelSize: 13; color: "white"; 
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
               id: textField10; objectName: "textField10"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField11; objectName: "textField11"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField12; objectName: "textField12"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField13; objectName: "textField13"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField14; objectName: "textField14"; width:61; height: 30; font.pixelSize: 13; color: "white";
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
               id: textField15; objectName: "textField15"; width:61; height: 30; font.pixelSize: 13; color: "white"; 
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

     Item {
          width: parent.width
          height: parent.height

          anchors.bottom: parent.bottom
          anchors.horizontalCenter: parent.horizontalCenter

          // TextArea bileşeni
          Rectangle {
              id: textArea
              width: 350
              height: 70
              anchors.horizontalCenter: parent.horizontalCenter
              anchors.bottom: parent.bottom
              anchors.bottomMargin: 70
              border.color: "blue"
              border.width: 2
              color: "transparent"

              // TextArea bileşeni
              TextArea {
                  id: textInput
                  objectName: "textInput"
                  anchors.fill: parent
                  readOnly: true
                  background: null
                  font.pixelSize: 20
                  color: "#FF0000"
                  text: "" // Bu placeholder, metin alanının içinde görüntülenir.
              }
          }
     }
     
     
     CircularGauge {
          objectName: "speed_gauge"
          property real speedgauge_value: 0
          width: 370
          height: 370
          x: 338
          y: 15
          value: speedgauge_value
          maximumValue: 120.0
          minimumValue: 0.0

          style: CircularGaugeStyle {
               tickmarkInset: toPixels(0.04)
               minorTickmarkInset: tickmarkInset
               labelStepSize: 20
               labelInset: toPixels(0.23)
               
               property real xCenter: outerRadius
               property real yCenter: outerRadius
               property real needleLength: outerRadius - tickmarkInset * 1.25
               property real needleTipWidth: toPixels(0.02)
               property real needleBaseWidth: toPixels(0.06)
               property bool halfGauge: false
               
               function toPixels(percentage) {
                   return percentage * outerRadius;
               }
               
               function degToRad(degrees) {
                   return degrees * (Math.PI / 180);
               }
               
               function radToDeg(radians) {
                   return radians * (180 / Math.PI);
               }
               
               function paintBackground(ctx) {
                   if (halfGauge) {
                       ctx.beginPath();
                       ctx.rect(0, 0, ctx.canvas.width, ctx.canvas.height / 2);
                       ctx.clip();
                   }
               
                   ctx.beginPath();
                   ctx.fillStyle = "black";
                   ctx.ellipse(0, 0, ctx.canvas.width, ctx.canvas.height);
                   ctx.fill();
               
                   ctx.beginPath();
                   ctx.lineWidth = tickmarkInset;
                   ctx.strokeStyle = "blue";
                   ctx.arc(xCenter, yCenter, outerRadius - ctx.lineWidth / 2, outerRadius - ctx.lineWidth / 2, 0, Math.PI * 2);
                   ctx.stroke();
               
                   ctx.beginPath();
                   ctx.lineWidth = tickmarkInset / 2;
                   ctx.strokeStyle = "#222";
                   ctx.arc(xCenter, yCenter, outerRadius - ctx.lineWidth / 2, outerRadius - ctx.lineWidth / 2, 0, Math.PI * 2);
                   ctx.stroke();
               
                   ctx.beginPath();
                   var gradient = ctx.createRadialGradient(xCenter, yCenter, outerRadius * 0.8, xCenter, yCenter, outerRadius);
                   gradient.addColorStop(0, Qt.rgba(1, 1, 1, 0));
                   gradient.addColorStop(0.7, Qt.rgba(1, 1, 1, 0.13));
                   gradient.addColorStop(1, Qt.rgba(1, 1, 1, 1));
                   ctx.fillStyle = gradient;
                   ctx.arc(xCenter, yCenter, outerRadius - tickmarkInset, outerRadius - tickmarkInset, 0, Math.PI * 2);
                   ctx.fill();
               }
               
               background: Canvas {
                   onPaint: {
                       var ctx = getContext("2d");
                       ctx.reset();
                       paintBackground(ctx);
                   }
               
                   Text {
                       id: speedText
                       font.pixelSize: toPixels(0.3)
                       text: kphInt
                       color: "white"
                       horizontalAlignment: Text.AlignRight
                       anchors.horizontalCenter: parent.horizontalCenter
                       anchors.top: parent.verticalCenter
                       anchors.topMargin: toPixels(0.1)
               
                       readonly property int kphInt: control.value
                   }
                   Text {
                       text: "km/h"
                       color: "white"
                       font.pixelSize: toPixels(0.09)
                       anchors.top: speedText.bottom
                       anchors.horizontalCenter: parent.horizontalCenter
                   }
               }
               
               needle: Canvas {
                   implicitWidth: needleBaseWidth
                   implicitHeight: needleLength
               
                   property real xCenter: width / 2
                   property real yCenter: height / 2
               
                   onPaint: {
                       var ctx = getContext("2d");
                       ctx.reset();
               
                       ctx.beginPath();
                       ctx.moveTo(xCenter, height);
                       ctx.lineTo(xCenter - needleBaseWidth / 2, height - needleBaseWidth / 2);
                       ctx.lineTo(xCenter - needleTipWidth / 2, 0);
                       ctx.lineTo(xCenter, yCenter - needleLength);
                       ctx.lineTo(xCenter, 0);
                       ctx.closePath();
                       ctx.fillStyle = Qt.rgba(0.66, 0, 0, 0.66);
                       ctx.fill();
               
                       ctx.beginPath();
                       ctx.moveTo(xCenter, height)
                       ctx.lineTo(width, height - needleBaseWidth / 2);
                       ctx.lineTo(xCenter + needleTipWidth / 2, 0);
                       ctx.lineTo(xCenter, 0);
                       ctx.closePath();
                       ctx.fillStyle = Qt.lighter(Qt.rgba(0.66, 0, 0, 0.66));
                       ctx.fill();
                   }
               }
               
               foreground: null
          } 

          Text {
              id: textFieldSpeed
              objectName: "textFieldSpeed"
              font.pixelSize: 24
              color: "white"
              anchors.horizontalCenter: parent.horizontalCenter
              anchors.top: parent.bottom
              anchors.topMargin: -100
          }
     }
    
     // İkinci CircularGauge bileşeni
     CircularGauge {
          objectName: "wh_gauge"
          property real whgauge_value: 0
          width:210
          height:210
          x:820
          y:250
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
     Gauge {
         objectName: "temp_gauge"
         property real tempgauge_value: 0
         tickmarkStepSize: 20
         minorTickmarkCount: 4
         font.pixelSize: 15
         //anchors.centerIn: parent
         //anchors.horizontalCenterOffset: -7
         x:240  //hız göstergesinin koordinatları
         y:70
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
              anchors.topMargin: 0 // Üst kenarın altına boşluk bırakma    
         }
         
         style: GaugeStyle {
              valueBar: Rectangle {
                   color: "#0000ff"
                   implicitWidth: 28
              } 
              foreground: null
              
              tickmark: Item {
                 implicitWidth: 18
                 implicitHeight: 1
                 
                 Rectangle {
                        x: control.tickmarkAlignment === Qt.AlignLeft
                            || control.tickmarkAlignment === Qt.AlignTop ? parent.implicitWidth : -28
                        width: 28
                        height: parent.height
                        color: "#c8c8c8"
                        anchors.fill: parent
                        anchors.leftMargin: 3
                        anchors.rightMargin: 3
                   }
              }
             
              minorTickmark: Item {
                   implicitWidth: 8
                   implicitHeight: 1
                   
                   Rectangle {
                        x: control.tickmarkAlignment === Qt.AlignLeft
                            || control.tickmarkAlignment === Qt.AlignTop ? parent.implicitWidth : -28
                        width: 10
                        height: parent.height
                        color: "#cccccc"
                        anchors.fill: parent
                        anchors.leftMargin: 2
                        anchors.rightMargin: 4
                   }
              }
         }
     }
     /*
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
     }*/
    
     //Voltmeter gauge
     //
     CircularGauge {
            objectName: "volt_gauge"
            property real voltgauge_value: 0  //
            width:210 // göstergenin büyüklük kare olcak
            height:210
            //anchors.centerIn: parent
            x:30   //hız göstergesinin koordinatları
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

     /*
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
     }*/

     Gauge {

          objectName: "bt_gauge"
          property real btgauge_value: 0
          tickmarkStepSize: 20
          minorTickmarkCount: 4
          font.pixelSize: 15
          //anchors.centerIn: parent
          //anchors.horizontalCenterOffset: -7
          x:730   //hız göstergesinin koordinatları
          y:70
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
             anchors.topMargin: 0 // Üst kenarın altına boşluk bırakma
             
             
          }


          style: GaugeStyle {
               valueBar: Rectangle {
                    color: "#0000ff"
                    implicitWidth: 28
               }    

               foreground: null

               tickmark: Item {
                  implicitWidth: 18
                  implicitHeight: 1
                  

                  Rectangle {
                         x: control.tickmarkAlignment === Qt.AlignLeft
                             || control.tickmarkAlignment === Qt.AlignTop ? parent.implicitWidth : -28
                         width: 28
                         height: parent.height
                         color: "#c8c8c8"
                         anchors.fill: parent
                         anchors.leftMargin: 3
                         anchors.rightMargin: 3
                    }
               }

              minorTickmark: Item {
                    implicitWidth: 8
                    implicitHeight: 1

                    Rectangle {
                         x: control.tickmarkAlignment === Qt.AlignLeft
                             || control.tickmarkAlignment === Qt.AlignTop ? parent.implicitWidth : -28
                         width: 10
                         height: parent.height
                         color: "#cccccc"
                         anchors.fill: parent
                         anchors.leftMargin: 2
                         anchors.rightMargin: 4
                    }
               }
          }
    }
     
      
}

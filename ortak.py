import serial_port3
import veri_isleme 
import serial

baud_rate = 9600  # Seri port iletişim hızı
packet_size = 128  # Paket boyutu
buffer_size= 128 # Buffer boyutu

ports = serial.tools.list_ports.comports()
print("Kullanilabilir seri portlar:")
for idx, port in enumerate(ports, start=1):
    print(f"{idx}: {port.device}")

# Kullanıcıdan seri port seçmesini iste
selection = int(input("Baglanmak istediginiz seri portun numarasini girin: ")) - 1
selected_port = ports[selection].device


# Seri port bağlantısını oluştur
ser = serial.Serial(selected_port, baud_rate)

# istenilen boyutta bir döngüsel tampon oluştur
circular_buffer = serial_port3.CircularBuffer(buffer_size)


while(True):
    x = serial_port3.get_packet(ser, circular_buffer, packet_size)
    y = veri_isleme.volts_cells(x)
    print(y)





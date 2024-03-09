import serial
import serial.tools.list_ports

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = bytearray(size)
        self.start = 0
        self.end = 0
        self.full = False

    def append(self, data):
        for byte in data:
            if not self.full:
                self.buffer[self.end] = byte
                self.end = (self.end + 1) % self.size
                if self.end == self.start:
                    self.full = True

    def pop_packet(self, packet_size):
        packet = bytearray()
        while len(packet) < packet_size:
            if self.full or (self.end < self.start and self.end > 0):
                packet.append(self.buffer[self.start])
                self.start = (self.start + 1) % self.size
                if self.start == self.end:
                    self.full = False
            else:
                break
        if len(packet) == packet_size:
            return bytes(packet)
        else:
            return None

if __name__ == "__main__":
    # Kullanılabilir seri portları listele
    ports = serial.tools.list_ports.comports()
    print("Kullanilabilir seri portlar:")
    for idx, port in enumerate(ports, start=1):
        print(f"{idx}: {port.device}")

    # Kullanıcıdan seri port seçmesini iste
    selection = int(input("Baglanmak istediginiz seri portun numarasini girin: ")) - 1
    selected_port = ports[selection].device
    baud_rate = 9600  # Seri port iletişim hızı
    packet_size = 8  # Paket boyutu

    # Seri port bağlantısını oluştur
    ser = serial.Serial(selected_port, baud_rate)

    # 8 baytlık bir döngüsel tampon oluştur
    circular_buffer = CircularBuffer(8)

    try:
        while True:
            if ser.in_waiting > 0:
                # Seri porttan veriyi oku
                received_data = ser.read(ser.in_waiting)
                # Veriyi döngüsel tampona ekle
                circular_buffer.append(received_data)

                
                while circular_buffer.full:
                    packet = circular_buffer.pop_packet(packet_size)
                    if packet:
                        print("Alinan paket:", packet)
                        
                        hex_packet = " ".join([hex(byte) for byte in packet])
                        print("Hex paket:", hex_packet)

                    else:
                        break
    except KeyboardInterrupt:
        # ctrl+c yapınca kapanır
        print("Program kapatildi.")
        ser.close()   
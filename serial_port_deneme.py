import serial

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
    serial_port = "COM15"  # Kullanılacak seri portu buraya girin
    baud_rate = 9600  # Seri port iletişim hızı
    packet_size = 8  # Paket boyutu

    # Seri port bağlantısını oluştur
    ser = serial.Serial(serial_port, baud_rate)

    # 8 baytlık bir döngüsel tampon oluştur
    circular_buffer = CircularBuffer(8)

    try:
        while True:
            if ser.in_waiting > 0:
                # Seri porttan veriyi oku
                received_data = ser.read(ser.in_waiting)
                # Veriyi döngüsel tampona ekle
                circular_buffer.append(received_data)

                # Tamponun dolu olduğu sürece 8 baytlık paketler al
                while circular_buffer.full:
                    packet = circular_buffer.pop_packet(packet_size)
                    if packet:
                        print("Alınan paket:", packet)
                    else:
                        break
    except KeyboardInterrupt:
        print("Program kapatıldı.")
        ser.close()

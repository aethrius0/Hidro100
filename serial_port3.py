import serial
import serial.tools.list_ports

baud_rate = 9600  # Seri port iletişim hızı
packet_size = 128  # Paket boyutu
buffer_size= 128 # Buffer boyutu

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
    # paket oluşturur
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

 
def get_packet(ser,circular_buffer,packet_size):   
    while True:
        if ser.in_waiting > 0:
            # Seri porttan veriyi oku
            received_data = ser.read(ser.in_waiting)
            # Veriyi döngüsel tampona ekle
            circular_buffer.append(received_data)

                
            while circular_buffer.full:
                packet = circular_buffer.pop_packet(packet_size)
                if packet:
                    return packet
                else:
                    break


import serial
ser = serial.Serial('COM15')  # open serial port
print(ser.name)         # check which port was really used
print(ser.read(1024))     # write a string
ser.close()         # close port
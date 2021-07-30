import serial
from serial import Serial
from serial.serialutil import Timeout
import re

# ser = serial.Serial('COM5')
# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string


# serial.Serial('COM5', 9600, 8)
ser = serial.Serial('COM5', 9600, timeout = 5)
size = ser.readline()
# data = ser.read()

# res = re.findall("[a-z][A-Z][0-9]",size)
# print(res)

# print(data)
print(size)
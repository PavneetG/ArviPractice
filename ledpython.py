import serial
import time

ArduinoSerial = serial.Serial('com18',9600)
time.sleep(2)

ArduinoSerial.write('1')

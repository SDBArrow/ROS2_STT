import serial
import time

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)

while True:

    port.write('B'.encode('ascii'))
    time.sleep(1)

    port.write('R'.encode('ascii'))
    time.sleep(1)
    
    port.write('L'.encode('ascii'))
    time.sleep(1)

    port.write('F'.encode('ascii'))
    time.sleep(1)
import serial
import time

arduino = serial.Serial('COM5', 115200)

def test():
    while True:
        dataInput = input("Data: ")
        print(dataInput)
        arduino.write(bytes(dataInput, 'utf-8'))




while True:
    test()

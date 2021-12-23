import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
servo1 = board.get_pin('d:3:s')
servo1_2 = board.get_pin('d:4:s')

iter8 = pyfirmata.util.Iterator(board)
iter8.start()

def servowrite(angle, servo):
    servo.write(angle)
    time.sleep(0.015)

servowrite(180, servo1)
servowrite(180, servo1_2)

while True:
    if (input("Servo Selection ") == "1"):
        servowrite(max(60, min(int(input("Angle? ")), 180)), servo1_2)
        print("")

    elif (input("Servo Selection") == "2"):
        servowrite(max(60, min(int(input("Angle? ")), 180)), servo1)

import serial
import time

sr = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)

user_input = input("plz enter: H for on, L for off, q or Q to quit:")
while user_input != 'q' and user_input != 'Q':
    byte_command = encode(user_input)
    sr.writelines(byte_command) 
    time.sleep(0.5)
        
print('Exiting the program')
sr.close()

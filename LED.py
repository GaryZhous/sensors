import serial
import time

sr = serial.Serial('COM4', 9800, timeout=1) #COM4 port
time.sleep(2)

user_input = input("plz enter the command, H for on, L for off, q or Q is quit:")
while user_input != 'q' and user_input != 'Q':
    byte_command = encode(user_input)
    ser.writelines(byte_command) #send out a byte
    time.sleep(1) #time interval is 1 second
    user_input = input("plz enter the command, H for on, L for off, q is quit:")
        
print('Exiting the program')
sr.close()

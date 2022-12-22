import serial
import time
import matplotlib.pyplot as plt

sr = serial.Serial('COM4', 9600)
time.sleep(2)
count = 0
data =[]                      
while i < 50:
	b = sr.readline()         
  string_n = b.decode()   
	reading = float(string_n.rstrip())     
	data.append(reading)           
	time.sleep(0.1)            
  count += 1

ser.close()

plt.plot(data)
plt.xlabel('Time (s)')
plt.ylabel('Potentiometer Reading (v)')
plt.title('Potentiometer Reading vs Time')
plt.show()

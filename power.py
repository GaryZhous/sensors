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
	time.sleep(0.01)            
  count += 1

ser.close()

plt.plot(data)
plt.xlabel('Time (s)')
plt.ylabel('Power (Wh)')
plt.title('Power vs Time')
plt.show()

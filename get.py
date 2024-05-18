import serial
import time

# Open the serial port (replace 'COM8' with the appropriate port name)
s = serial.Serial('COM8', 115200)

# Read data indefinitely
time.sleep(1)
while (grbl_out != "Grbl 1.1f ['$' for help]"):
    s.write("?".encode())
    grbl_out = s.readline()  # Read the available data
    try :
        print(grbl_out.strip().decode().split('|')[1])
    except :
        print(grbl_out.strip().decode())

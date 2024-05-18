import serial
import time
axis = input("Home Axis :")
while(axis != ("X" or "Y" or "Z")):
    axis = input("Enter valid Axis (X,Y, or Z) :")
pos = 0
# Replace 'COM8' with the correct COM port for your CNC controller
ser = serial.Serial('COM8', 115200)
time.sleep(0.5)  # Wait for the connection to stabilize
while True:
    user_input = input("Enter (est) remaining dist, 0 to stop :")
    try :
        while(int(user_input) <= 0):
            user_input = input("Enter non-negative number :")
    except :
        user_input = input("Enter valid positive number :")
    try :
        pos = pos - int(user_input)
    except :
        print("type a number") #in case of invalid input
    gcode_command = f"G0 {axis}{pos}\r\n"
    ser.write(gcode_command.encode())  # Send the G28 command (home X-axis to -10)
    if user_input == 0:
        ser.close()  # Close the serial connection
        break






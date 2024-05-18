import serial
import time

# Replace 'COM8' with the correct COM port for your CNC controller
ser = serial.Serial('COM8', 115200)
time.sleep(2)  # Wait for the connection to stabilize

# Encode the G-code command as bytes
gcode_command = "G0 X-10\r\n".encode()
ser.write(gcode_command)  # Send the G28 command (home X-axis to -10)

time.sleep(1)  # Wait for the command to complete
ser.close()  # Close the serial connection

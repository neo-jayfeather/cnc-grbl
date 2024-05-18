import serial
import time
userInput = ''
s = serial.Serial('COM8', 115200)
def get():
    time.sleep(0.25)
    grbl_out = ''
    stop = False
    while (grbl_out != "Grbl 1.1f ['$' for help]" and stop == False):
        s.write("?".encode())
        stop = False
        grbl_out = s.readline()  # Read the available data
        try :
            print(grbl_out.strip().decode().split('|')[1])
            stop = True
        except :
            print(grbl_out.strip().decode())
def set(command):
    command = command + "\r\n"
    time.sleep(0.25)
    s.write(command.encode()) #send bytes
    grbl_out = s.readline() #read bytes
    print(grbl_out.strip().decode())
while(userInput != 0):
    userInput = input("G-Code Command, 0 to stop :")
    if(userInput == "get"):
        get()
    else:
        set(userInput)


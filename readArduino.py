import serial
import time

'''
This is for a raspberry pi.

Both Arduino_port and output_file will need to be change for windows.

Arduino_port need to be found once the pi is linked up to the arduino
'''
arduino_port = '/dev/ttyUSB0' #place holder
baud_rate = 9600  
output_file = '/home/{user}/Documents/arduino_data.log'  #place holder

try:
    
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"Connected to Arduino on {arduino_port}")

    with open(output_file, 'a') as file:
        while True:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(data)  
                file.write(data + '\n')  
except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial connection closed.")

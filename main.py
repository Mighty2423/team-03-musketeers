import serial
import carwreck
import earthquake
import floods
import hurricane
import tornado
import wildfire





def main():

  # Open the serial port
  ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with your port name and 9600 with the baud rate


  # Write data
  # ser.write(b'Hello from Python!\n')



  # Read data
  data = ser.readline()
  print(data.decode('utf-8'))

  # Close the port
  ser.close()


if __name__ == "__main__":
  main()
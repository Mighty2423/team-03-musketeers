import serial
import time

# Open connection
srl = serial.Serial(serial_port, baud_rate, timeout=1)
try:
    while True:
        # Wait for input
        if srl.in_waiting > 0:
            # Read input
            received_data = srl.readline().decode('utf-8').strip()
            print(f"{received_data}")

            # Respond
            reply = "okay"
            srl.write(reply.encode('utf-8'))
            print(f"{reply}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("serial communication stopped.")
finally:
    srl.close()
import asyncio
import serial_asyncio

# Setup
serial_port = 'COM7'
baud_rate = 115200
num_choices = 0

# Variable for User Input from Micro-controller
user_in = []

# Function to monitor the serial in and store input for later
async def serial_monitor(reader):
    # continuously check if there is any input
    while True:
        # Read Function
        data_in = await reader.readline()
        data_in = data_in.decode('utf-8').strip()
        # Add input to list
        user_in.append(data_in)

# Function to send output over serial
async def send_UART(writer, num_choices):
    # Bounds Check
    if 0 < num_choices < 6:
        # Send over UART
        UART_string = f'{num_choices}\n' 
        writer.write(UART_string.encode())
        # Wait 'till sent
        await writer.drain()


async def sync_with_external(num_of_choices, writer):
    await send_UART(writer, num_of_choices)
    response = False
    while(not response):
        print("Waiting for response...")
        await asyncio.sleep(5)
        if user_in:
            value = user_in[0]
            user_in.clear()
            response = True
            return value
    print("Response received")
            


# Main Function
# async def main_(reader, writer):
#     ...
    # no_response = 0
    # while True:
    #     # Main Routine Loop
    #     # TODO - HERE IS WHERE THE MAIN PROGRAM WILL GO

    #     # userchoice(numofchoices, writer)
    #     # Placeholder Main
    #     num_send = 2                            # Example sending number
    #     await send_UART(writer, num_send)       # Example sending function
    #     no_response = 1
    #     while(no_response):                     # Example pending loop
    #         # Wait Seconds for Response
    #         print(f'waiting response...')
    #         await asyncio.sleep(5)                  # Example wait    
    #         if user_in:                             # Example check if
    #             for user_input in user_in:
    #                 # TODO - Handle input
    #                 print(f'{user_input}\n')
    #             # Clear for next in
    #             user_in.clear()
    #             no_response = 0
    #     print(f'response received.')
    
# Program Main
# async def main():
#     # Define Serial Communication
#     reader, writer = await serial_asyncio.open_serial_connection(url=serial_port, baudrate=baud_rate)
#     # Async Task switching
#     await asyncio.gather(serial_monitor(reader), main_(reader, writer))



#         # END OF MAIN LOOP
# if __name__ == '__main__':
#     asyncio.run(main())

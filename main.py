import serial
# import earthquake
# import floods
# import hurricane
# import tornado
import wildfire

# Utility function for viewing data
def print_k_v(dictionary):
  for k, v in dictionary.items():
    print(f"{k}: ")
    if not isinstance(v, dict):
      print(v, end="\n\n")
    else:
      print_k_v(v)


def poll(serial_port, integer, prompt):
  print(prompt)
  serial_port.write(integer)

  choice = int(serial_port.read())

  return choice


def get_menu_list(menu):
  menu_list = []
  for k, v in menu:
    if k != "message":
      menu_list.append(k)
  return menu_list


def print_menu(menu_list):
  for i in range(len(menu_list)):
    print(f"{i}: {menu_list[i]}")


def get_choice(menu):
  menu_list = get_menu_list(menu.items())

  prompt = "Choose an option: "

  valid = False
  while(not valid):
    print_menu(menu_list)
    choice = input(prompt)

    try:
      choice = int(choice)
      if choice < 0 or choice > len(menu_list)-1:
        raise Exception()
      else: # If successful!
        valid = True
        return menu[menu_list[choice]]
    except Exception:
      print("Invalid choice", '\n')
      prompt = "Please choose a valid option: "

def main_menu(disasters):
  prompt = "Choose your adventure: "

  valid = False
  while(not valid):
    for i in range(len(disasters)):
        print(f"{i}: {disasters[i].__name__.capitalize()}")
    print(f"{len(disasters)}: Quit")

    choice = input(prompt)
    print("\n", f"You chose {choice}", sep='')

    try:
      choice = int(choice)
      if choice < 0 or choice > len(disasters):
        raise Exception("Out of range")
      else: # If successful!
        valid = True
        return choice
    except Exception:
      print("Invalid choice")
      prompt = "Please choose a valid option: "


def main():
  # disasters = [earthquake, floods, hurricane, tornado, wildfire]
  disasters = [wildfire]

  quit = False
  while(not quit):
    play = False
    
    choice = main_menu(disasters)

    if choice == len(disasters):
      print('Thanks for playing! Stay safe!')
      quit = True
    else:
      play = True
      current_menu = disasters[choice].get()['At home']

    while(play):
      if "You die" in current_menu['message'] or "safe" in current_menu['message']:
        print('\n', current_menu['message'], '\n', sep='')
        play = False
      else:
        print('\n', current_menu['message'])
        current_menu = get_choice(current_menu)
    


# def main():

#   # Open the serial port
#   ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with your port name and 9600 with the baud rate


#   # Write data
#   # ser.write(b'Hello from Python!\n')



#   # Read data
#   data = ser.readline()
#   print(data.decode('utf-8'))

#   # Close the port
#   ser.close()


if __name__ == "__main__":
  main()
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
      if choice < 0 or choice > len(menu_list):
        raise Exception()
      else:
        valid = True
        return menu[menu_list[choice]]
    except Exception:
      print("Invalid choice")
      prompt = "Please choose a valid option: "



def main():
  disasters = [wildfire]

  # choice = disasters[4].get()
  # print_k_v(choice)
  # print(choice)



  quit = False
  while(not quit):
    
    # for i in range(len(disasters)):
    #   print(f"{i}: {disasters[i].__name__}")

    choice = wildfire.get()["At home"]

    print(get_choice(choice))

    play = True
    while(play):
      ...

      play = False


    quit = True
    


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
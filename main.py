from serialio import *
import earthquake
import floods
import hurricane
import tornado
import wildfire

# Utility function for viewing data
def print_k_v(dictionary):
  for k, v in dictionary.items():
    print(f"{k}: ")
    if not isinstance(v, dict):
      print(v, end="\n\n")
    else:
      print_k_v(v)

# Needs work/to be integrated in place of input(prompt)
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


def get_choice(menu, writer):
  menu_list = get_menu_list(menu.items())

  prompt = "Choose an option: "

  valid = False
  while(not valid):
    print_menu(menu_list)
    choice = sync_with_external(len(menu_list), writer)

    try:
      choice = int(choice)
      if choice < 0 or choice > len(menu_list)-1:
        raise Exception()
      else: # If successful!
        valid = True
        return menu[menu_list[choice]]
    except Exception:
      print("Invalid choice", '\n')
      prompt = "Please choose a valid option (e.g. 0 or 1): "

def main_menu(disasters, writer):
  prompt = "Choose your adventure: "

  valid = False
  while(not valid):
    for i in range(len(disasters)):
        print(f"{i}: {disasters[i].__name__.capitalize()}")
    print(f"{len(disasters)}: Quit")

    choice = sync_with_external(len(disasters), writer)
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
      prompt = "Please choose a valid option (e.g. 0 or 1): "


async def main_(reader, writer):
  disasters = [earthquake, floods, hurricane, tornado, wildfire]

  quit = False
  while(not quit):
    play = False
    
    choice = main_menu(disasters, writer)

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
        print('\n', current_menu['message'], sep='')
        current_menu = get_choice(current_menu, writer)

async def main():
  reader, writer = await serial_asyncio.open_serial_connection(url=serial_port, baudrate=baud_rate)

  await asyncio.gather(serial_monitor(reader), main_(reader, writer))

if __name__ == "__main__":
  asyncio.run(main())
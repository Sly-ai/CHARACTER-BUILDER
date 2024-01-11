print("Day 27 Challenge")
print()
import os, time, random


def character():
  os.system('clear')
  print("Welcome to the Character Creator!")
  time.sleep(1)
  print("Please enter the following information:")
  time.sleep(1)
  name = input("Hero name: ")
  charType = [
    'human', 'imp', 'wizard', 'elf', 'dwarf', 'gnome', 'orc', 'goblin',
    'dwarf', 'halfling'
  ]
  print()
  print("Your character is:")
  print(f"Name: \033[1m{name} \033[0m")
  print(f"Type: \033[1;35m {random.choice(charType).upper()} \033[0m")
  print()


def health():
  six_sided_dice = random.randint(1, 6)
  twelve_sided_dice = random.randint(1, 12)
  health_stat = ((six_sided_dice * twelve_sided_dice) / 2) + 10
  return health_stat


def strength():
  six_sided_dice = random.randint(1, 6)
  eight_sided_dice = random.randint(1, 8)
  strength_stat = ((six_sided_dice * eight_sided_dice) / 2) + 12
  return strength_stat


while True:
  character()
  print('Health: \033[0;32m',health(),'\033[0m')
  print('Strength: \033[1;34m', strength(),'\033[0m')
  print()
  tryagain = input("Y/N> ")
  if tryagain == "N" or tryagain == 'n':
    print('See you next time')
    break
    exit()

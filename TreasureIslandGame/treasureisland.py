print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# 3 ``` means that there are many lines to come in String form.

choice = input("You are at a cross road. Where do you want to go?\nType 'left or 'right'\n")

if choice == "left":
    boat_choice = input("You have come to a lake. There is an island in the middle of lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if boat_choice == "wait":
        print("Which door?")
        door_options = input("You are in front of three doors. Type 'blue', 'yellow' or 'red'")
        if door_options == "blue":
            print("You win! You have found the treasure!")
        elif door_options == "blue":
            print("You are eaten by beasts.\nGame Over!")
        elif door_options == "red":
            print("You are burned by fire.\nGame Over!")
        else:
            print("Invalid choice. Game Over!")
    elif boat_choice == "swim":
        print("You are attacked by trout.\nGame Over!")
    else:
        print("Invalid choice. Game Over!")
elif choice == "right":
    print("You have fallen into a hole!\nGame Over!")
else:
    print("Invalid choice. Game Over!")

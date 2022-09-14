print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
play_again = 1
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? 'Left' or 'Right': ").lower()
if direction == 'left':
    way = input(
        "You come at a lake.There is an island in the middle of the lake. Type 'wait' to wait for the boat or type "
        "'swim' to swim across ").lower()
    if way == 'swim':
        print("You were eaten by a shark. Game over!")
    elif way == 'wait':
        door = input("You arrive at the island unharmed.There is a house with 3 doors.One red, one yellow and one "
                     "blue. Which color do you choose? ").lower()
        if door == 'yellow':
            print("You found the treasure. Yayayyyy!!")
        elif door == 'blue':
            print("You entered a room full of beast. Game Over!")
        elif door == 'red':
            print("You entered a room full of fire. Game Over!")
elif direction == 'right':
    print('You fell of the cliff. Game Over!')


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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. And Gain fifteen Points") 

print("You walk into a castle.")
a = "sword"
b = "battleaxe"

print(f"Two weapons are in the armory. Which will you choose: weapon a ({a}) or weapon b ({b})?")

weapon = input(f"Enter weapon of choice ({a}/{b}): ")
print(f"You have chosen: {weapon}")

if weapon.lower() == a:
    print("The sword gleams with ancient magic. You feel faster and more agile.")
elif weapon.lower() == b:
    print("The battle axe hums with raw power. You feel unstoppable.")
else:
    print("You hesitate... and the castle begins to shift around you. \n You Died Because Of Indecisiveness? ")
speed = 5
strength = 5


if weapon.lower() == a:
    speed += 4
elif weapon.lower() == b:
   strength += 4

print(f"Your updated stats: Strength = {strength}, Speed = {speed}")

left_gate = "You opened the left gate. It teleported you to a boss battle with the Troll!"
right_gate = "You opened the right gate. It teleported you to a mini battle with Gnomes."

choice = input(f"Which gate will you enter? Left or Right: ").lower()

print(f"you have chosen: ({choice})")

if choice == "left":
    print(left_gate)
elif choice == "right":
    print(right_gate)
else:
    print("You wander between the gates... and vanish into the void.")

battle_with_troll = "I have defeated you. You Vile Creature."
fight_with_gnomes = "You Ugly Pricks I Rid the World from your Nasty Greed Of Gold. Diee!!!!!"

if choice == "left":
    if strength > 5:
        print(f"you win.\n {battle_with_troll}\n You Get A Chest After Defeeating The monsters. \n The chest is filled with Gold.You gain +15 points and unlock the Treasure Hunter title!")
    else:
        print("you lose")
elif choice == "right":
    if speed > 5:
        print(f"you win.\n {fight_with_gnomes}\n You Get A Chest After Defeeating The monsters. \n The chest is filled with Gold.You gain +15 points and unlock the Treasure Hunter title!")
    else:
        print("you lose")
else:
    print("You Died")

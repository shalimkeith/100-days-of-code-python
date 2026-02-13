import random 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock,paper,scissors]

user_choice =int(input("Choose:  0 For Rock, 1 for Paper And 2 for Scissors: \n"))

if user_choice > 2 or user_choice < 0:
    print("you Choose Incorrect value")
    exit()
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer choose:\n{computer_choice}")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You won!")
elif user_choice >=3 or user_choice < 0 :
    print("Incorrect Number")
elif computer_choice > user_choice:
    print("You Lose")
elif computer_choice == user_choice:
    print("Draw")
elif computer_choice == 0 and user_choice == 1:
    print("You won!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
elif computer_choice == 1 and user_choice == 2:
    print("You won!")
else:
    print("Invalid Statement")
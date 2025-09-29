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


user_choice = input("Choose:  0 For Rock, 1 for Paper And 2 for Scissors: \n")

computer_choice = random.randint(0,2)
print(f"Computer choose:\n{computer_choice}")

if

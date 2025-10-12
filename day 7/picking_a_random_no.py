import random

word_list = ["ardvark","baboon","cow"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess_a_letter = input("guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess_a_letter:
        print("Right")
    else:
        print("Wrong")
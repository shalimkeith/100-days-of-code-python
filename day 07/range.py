import random

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in range(len(chosen_word)):
    display += "_"
print(display)
while "_" != True:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        '''print(f"Current position : {position}\n Current letter {letter}\n Guessed letter: {guess}\n")'''
        if letter == guess:
            display[position] = letter
    print(display)
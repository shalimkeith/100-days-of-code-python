import random
import hangman_art
import hangman_words


print(hangman_art.welcome)



chosen_word = random.choice(hangman_words.words_list)  
word_length = len(chosen_word)

lives = 6

print(f'Pssst, the solution is {chosen_word}.')  


display = ["_"] * word_length
print(" ".join(display))

end_of_game = False


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess} this letter.")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a Life.☠️")
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position].lower() == guess: 
                display[position] = guess
    else:
        lives -= 1
        print(f"You have {lives} lives left.")
   

    print(f"{' '.join(display)}")
   

    if "_" not in display:
        end_of_game = True
        print("******You Win*******")

    if lives == 0:
        end_of_game = True
        print("You lose! The word was:", chosen_word)

    print(hangman_art.stages[lives])
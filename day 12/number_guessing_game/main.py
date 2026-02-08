from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
	""""checks answers against guesses and returns the number of turns remaining"""
	if guess > answer:
		print("Too high.")
		return turns - 1
		
	elif guess < answer:
		print("Too low.")
		return turns - 1
	else:
		print(f"You are correct. The answer was {answer}.")
	
def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def game():
	print("Welcome to the guessing game!!! \nI am thinking of a number between 1 and 100.")
	answer = randint(1,100)


	turns = set_difficulty()
	guess = 0

	while guess != answer:
		
		print(f"You have {turns} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		turns = check_answer(guess,answer,turns)
		if turns == 0:
			print("You have lost the game,\n8***** Loser****8.")
			return exit
		
		
game()

# if answer is write repeat the game or exit
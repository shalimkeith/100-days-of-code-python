print("welcome to the love calculator!")
name1 = input("Enter First name? \n")
name2 = input("Enter Second name? \n")

combined_names = (name1 + name2).lower()

true_score = 0

for letter in "true":
    true_score += combined_names.count(letter)

love_score = 0

for letter in "love":
    love_score += combined_names.count(letter)

love_score_str = str(true_score) + str(love_score)

score = int(love_score_str)
if score > 80:
    print(f"Your score is {score}. 🔥 Legendary bond! Your love arc rivals the greatest cinematic romances.")
elif score > 50:
    print(f"Your score is {score}. 💫 Promising quest! With effort, this could be epic.")
else:
    print(f"Your score is {score}. 🧊 Cold start. Might need a side quest to warm things up.")

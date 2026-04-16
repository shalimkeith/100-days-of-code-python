sentence = "What is the Airspeed Velocity of an Unladon Swallow?"

words = sentence.split()

result = {word:len(word) for word in words if "" in word}

print(result)

sentence = "What is the Airspeed Velocity of an Unladon Swallow?"


result = {word:len(word) for word in sentence.split()}

print(result)

# txt = "apple#banana#cherry#orange"
#
# x = txt.split("#")
#
# print(x)

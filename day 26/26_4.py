# sentence = "What is the Airspeed Velocity of an Unladon Swallow?"
#
# words = sentence.split()
#
# result = {word:len(word) for word in words if "" in word}
#
# print(result)

sentence = "And in my Dreams I caught you?"


result = {word:len(word) for word in sentence.split()}

print(result)

# txt = "apple#banana#cherry#orange"
#
# x = txt.split("#")
#
# print(x)

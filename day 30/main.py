# try:
#     file = open('file.txt')
#     dictionary = {"key" : "value"}
#     print(dictionary ["key"])
# except FileNotFoundError:
#     file = open('file.txt', 'w')
#     file.write("Print")
#
# except KeyError as error_message:
#     print(f"key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#
#     raise TypeError("This is an error i made up.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Humans are not that tall. Usually...")


bmi = weight / height ** 2
print(bmi)


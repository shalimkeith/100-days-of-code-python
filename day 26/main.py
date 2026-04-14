# name = "Keith"
# new_list = [letter for letter in name]
#
# name = "Keith"
# new_list = [letter for letter in name]
# print(new_list)
#
# name = "LEmiso"
# letter_list = [letter for letter in name]
# print(letter_list)
#
# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)
#
# names = ["Alex", "Eleanor", "Beatrix"]
# print(names)
#
# short_names = [name for name in names if len(name) > 4]
# print(short_names)
#
# names = ["alice", "BOB", "charlie"]
# caps_list = [name.upper() for name in names]
# print(caps_list)

# numbers = [1,1,2,3,5,8,13,21,34,55]
#
# squared_numbers = [num ** 2 for num in numbers]
#
# print(squared_numbers)

#printin even numbers
# numbers = [1,1,2,3,5,8,13,21,34,55]
#
# result = [num for num in numbers if num % 2 == 0]
#
# print(result)
#
# with open("file1.txt", "r") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt", "r") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num  in file_2_data]
# print(result)

#print(result)`

# with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()

# for i in range(max(len(lines1), len(lines2))):
#     if i < len(lines1) and i < len(lines2):
#         if lines1[i] == lines2[i]:
#             print(f"Same at line {i+1}:")
#             print("File1:", lines1[i].strip())
#             print("File2:", lines2[i].strip())
#     elif i < len(lines1):
#         print(f"Extra line in file1 at {i+1}: {lines1[i].strip()}")
#     else:
#         print(f"Extra line in file2 at {i+1}: {lines2[i].strip()}")

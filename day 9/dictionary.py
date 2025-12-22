programming_dictionaries = {
    "Bug":"An error in a program that prevents sthe program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again",
    
}

#print(programming_dictionaries)
#print(programming_dictionaries["Function"])
programming_dictionaries["Loop"] = "The action of doing something over and over again"
#print(programming_dictionaries)
#create a dictionary
empty_dictionary = {}
#wiping a dictionary
#programming_dictionaries= {}
#Editing a dictionary
programming_dictionaries["Bug"] = "hi my name is keith"
#print(programming_dictionaries)

#looping in a dictionary

for  key in programming_dictionaries:
    print(key)
    print(programming_dictionaries[key])
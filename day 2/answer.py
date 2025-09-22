# Prompt the user for a two-digit number
number= int(input("Enter a two-digit number: "))

# Extract the digits and calculate their sum
digit_sum = (number // 10) + (number % 10)

# Display the result
print(f"The sum of the digits is: {digit_sum}")

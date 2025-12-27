from art import logo
print(logo)

print()

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1= round(float(input("What is the first number?: ")),2)

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue == True:
        operations_symbol = input("pick an operation to perform from the above list: ")
        num2= round(float(input("What is the next number?: ")),2)
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input(f"type 'y' to continue with the {answer}, or type 'n' to start a new calculation type ''.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
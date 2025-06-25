#Define a function that takes three arguments two numbers and an operator(+,-,*,/)
    # define calculator
def main ():
    calculator()

def calculator():
    print("")
    num1 = int(input("Enter the first number: "))
    print("")
    operator = input("Choose operator (+,-.*,/): ")
    print("")
    num2 = int(input("Enter the second number: "))
    print("")

    if operator == '+':
        result = num1 + num2
        print(f"{num1} {operator} {num2} = {result}")
        print("")
    
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} {operator} {num2} = {result}")
        print("")
        
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} {operator} {num2} = {result}")
        print("")
    
    elif operator == '/':
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
        print("")
    
    else:
        print ("Wrong operator")
        print("")
        print ("Choose between (+,-,*,/)")
    
if __name__ == '__main__':
    main()
#class basic calculator
class Calculator:
    #Add funcion two numbers
    def add(self, x, y):
        return x + y
    #Sub funcion two numbers
    def subtract(self, x, y):
        return x - y
    #Mul funcion two numbers
    def multiply(self, x, y):
        return x * y
    #Div funcion two numbers
    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero!"
        return x // y

calculator = Calculator()


print("Select a choice:")
print("A. Add")
print("S. Subtract")
print("M. Multiply")
print("D. Divide")
#select choice, if you enter in lower it will do it in uppar 
choice = input("Enter choice (A/S/M/D): ").upper()
#take input of 2 numbers, first number and second number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#choice
if choice == 'A':
    result = calculator.add(num1, num2)
    operation = "+"
elif choice == 'S':
    result = calculator.subtract(num1, num2)
    operation = "-"
elif choice == 'M':
    result = calculator.multiply(num1, num2)
    operation = "*"
elif choice == 'D':
    result = calculator.divide(num1, num2)
    operation = "/"
else:
    print("Invalid choice")
    exit()

print(f"{num1} {operation} {num2} = {result}")

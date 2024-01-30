# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and printing the result
result = add_numbers(num1, num2)
print("The sum of {} and {} is: {}".format(num1, num2, result))

# Function to add three numbers
def add_numbers(num1, num2, num3):
    return num1 + num2 + num3

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calling the function and printing the result
result = add_numbers(num1, num2, num3)
print("The sum of {}, {}, and {} is: {}".format(num1, num2, num3, result))

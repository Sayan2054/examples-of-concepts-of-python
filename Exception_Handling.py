# Example of Exception handling:-

# main.py

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result of the division is:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
'''output:-
Enter the first number: 10
Enter the second number: 0
Division by zero is not allowed.
'''



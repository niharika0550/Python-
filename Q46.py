#Q46. Write a python code to demonstrate try and except.

try:
   number = int(input("Enter a number: "))
   result = 10 / number

except ZeroDivisionError:
   print("Error: Cannot divide by zero.")

except ValueError:
   print("Error: Invalid input, Enter a valid number.")

print("\nThis program is executed by Niharika")
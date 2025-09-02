#Q47. Write a python code to demonstrate try and except and else.

try:
   number = int(input("Enter a number: "))
   result = 10 / number

except ZeroDivisionError:
   print("Error: Cannot divide by zero.")

else:
   print(f"The result is {result}.")

print("\nThis program is executed by Niharika")
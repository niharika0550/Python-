#Q48. Write a python code to demonstrate try and except and finally.

try:
  file = open('example.txt', 'r')
  content = file.read()

except FileNotFoundError:
   print("Error: The file was not found.")

finally:
   file.close()

print("\nThis program is executed by Niharika")
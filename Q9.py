#Q9. Write python code to demonstrate some of core objects and functions.

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = user_input.split()
numbers = list(map(int, input_list))
total = sum(numbers)
length = len(numbers)
sorted_numbers = sorted(numbers)

print(f"Original list of numbers: {numbers}")
print(f"Sum of numbers: {total}")
print(f"Number of elements: {length}")
print(f"Sorted list of numbers: {sorted_numbers}")

print("\nThis program is executed by Niharika")
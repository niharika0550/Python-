#Q20. Write python code to print all the perfect numbers from 1-2025. Also print the total count.

count = 0
print("Perfect Numbers from 1 to 2025:")

for num in range(1, 2026):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(num, end=" ")
        count += 1

print("\nTotal Perfect Numbers:", count)

print("\nThis program is executed by Niharika")
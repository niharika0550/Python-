#Q15. Write python code to check whether the given number is perfect number or not.

n = int(input("Enter number: "))
sum_div = sum([i for i in range(1, n) if n % i == 0])
if sum_div == n:
    print("Perfect number")
else:
    print("Not a perfect number")
print("\nThis program is executed by Niharika")
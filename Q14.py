#Q14. Write python code to check whether given year is Leap year or not.

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
print("\nThis program is executed by Niharika")
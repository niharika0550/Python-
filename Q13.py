#Q13. Write python code to calculate your age on given date.

from datetime import date

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

today = date.today()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
print("Your age is:", age)
print("\nThis program is executed by Niharika")
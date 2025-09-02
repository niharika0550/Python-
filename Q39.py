# Q39. Write a python code to calculate income tax for the input income by adhering to the rules.
# •	There is no tax on income till Rs. 2,50,000
# •	5% on between Rs. 2,50,001 to Rs. 5,00,000
# •	10% on between Rs. 5,00,001 to Rs. 10,00,000
# •	20% on between Rs. 10,00,001 to Rs. 20,00,000
# •	30% on between Rs. 20,00,001 to Rs. 30,00,000
# •	40% on above Rs. 30,00,001

income = float(input("Enter your income: "))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.10
elif income <= 2000000:
    tax = (250000 * 0.05) + (500000 * 0.10) + (income - 1000000) * 0.20
elif income <= 3000000:
    tax = (250000 * 0.05) + (500000 * 0.10) + (1000000 * 0.20) + (income - 2000000) * 0.30
else:
    tax = (250000 * 0.05) + (500000 * 0.10) + (1000000 * 0.20) + (1000000 * 0.30) + (income - 3000000) * 0.40

print(f"Your Income: Rs. {income:.2f}")
print(f"Income Tax: Rs. {tax:.2f}")

print("\nThis program is executed by Niharika")
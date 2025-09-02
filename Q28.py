# Q28. Write python code to print the following pattern.
#     A
#    AB
#   ABC
#  ABCD
# ABCDE

for i in range(1, 6):
    print(" " * (5 - i) + "ABCDE"[:i])

print("\nThis program is executed by Niharika")
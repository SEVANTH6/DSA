# Largest Of three Number.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Number Number: "))

if num1 > num2 & num1 > num3:
    print(f"{num1} is greater.")
elif num2 > num1 & num2 > num3:
    print(f"{num2} is greater.")
else:
    print(f"{num3} is greater.")
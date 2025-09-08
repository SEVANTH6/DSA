# Check the Number is Odd or even

def Odd_Even():
    number = int(input("Enter a Number: "))

    if (number % 2 == 0):
        print(f"{number} is a Even Number")
    else:
        print(f"{number} is a Odd Number")

Odd_Even()
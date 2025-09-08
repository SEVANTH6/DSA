# Check if the number is divisible by the number User give

def divisible_calculator():
    n = int(input("Enter the number u want to check: "))
    d = int(input("Enter the divisor: "))

    if d == 0:
        print(f"0 divisor is not allowed...")
    elif (n % d == 0):
        print(f"{n} can is divisible by {d}")
    else:
        print(f"{n} Can not divisible by {d}")

divisible_calculator()
# Multiplication Table

def Multiplication_table():
    n = int(input("Enter the Table You want to Print: "))
    r = int(input("Enter the Range: "))

    for i in range(1, r + 1):
        print(f"{n} * {i} = {n * i}")

Multiplication_table()
# *
# **
# ***
# ****
# *****


def Pattern():
    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
Pattern()

# Mistakes:
# Consider the staring number 1 . if not it will consider the first i to be 0 that print nothing.
# if i gave 5 as a input it only take 4 becouse in python the range not consider the stop elemnt. So in the program i considered N + 1 for row.
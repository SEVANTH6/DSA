# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


def Pattern():
    n = int(input("Enter number of rows: "))

# For Rows
    for i in range(n):
        # For column 
        for j in range(n):
            print("*", end= " ") # end = "" used as for continue printing in the same line otherwise python print function print in next line.
        print("") #Print in outer loop.

Pattern()




# def Pattern():
#     n = int(input("Enter number of rows: "))
#     for i in range(n):
#         for j in range(n):
#             print("* ")
# Pattern()


# ---3 mistakes are---:
# Didn’t use end=" "
# Forgot print() after inner loop
# Added an extra space inside "* " instead of controlling with end
# Putting print("") inside the inner loop instead of after it.

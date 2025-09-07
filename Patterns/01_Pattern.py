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


# ---------------------------------Trace-------------------------------------:
# if n = 5
# i = 0(ROW): (True)
#     j = 0:  index 0 = *
#     j = 1:  index 1 = **
#     j = 2:  index 2 = ***
#     j = 3:  index 3 = ****
#     j = 4:  index 4 = *****
# i INCREMENTS

# Pattern: 
# *****

# i = 1(ROW): (True)
#     j = 0:  index 0 = *
#     j = 1:  index 1 = **
#     j = 2:  index 2 = ***
#     j = 3:  index 3 = ****
#     j = 4:  index 4 = *****
# i INCREMENTS

# Pattern: 
# *****
# *****

# i = 2(ROW): (True)
#     j = 0:  index 0 = *
#     j = 1:  index 1 = **
#     j = 2:  index 2 = ***
#     j = 3:  index 3 = ****
#     j = 4:  index 4 = *****
# i INCREMENTS

# Pattern: 
# *****
# *****
# *****

# i = 3(ROW): (True)
#     j  index 0 = *
#     j  index 1 = **
#     j  index 2 = ***
#     j  index 3 = ****
#     j  index 4 = *****
# i INCREMENTS

# Pattern: 
# *****
# *****
# *****
# *****

# i = 4(ROW): (True)
#     j = 0:  index 0 = *
#     j = 1:  index 1 = **
#     j = 2:  index 2 = ***
#     j = 3:  index 3 = ****
#     j = 4:  index 4 = *****

# Pattern: 
# *****
# *****
# *****
# *****
# *****

# i = 5(ROW): (False) (Python Not consider Stop index)

# --Final Pattern:--
# *****
# *****
# *****
# *****
# *****

# -------------------------------------------------------------------------------------------------

# ---3 mistakes are---:
# Didn’t use end=" "
# Forgot print() after inner loop
# Added an extra space inside "* " instead of controlling with end
# Putting print("") inside the inner loop instead of after it.

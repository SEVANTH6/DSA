# *****
# ****
# ***
# **
# *

def Pattern():
    n = int(input("Enter Number of Rows: "))

    for i in range(n): 
        for j in range(n - i): 
            print("*", end= " ")
        print()
Pattern()

# ---------------------------------Trace-------------------------------------:
# if n = 5:

# i = 0
#     j = 0 : index 0 = *
#     j = 1 : index 0 = **
#     j = 2 : index 0 = ***
#     j = 3 : index 0 = ****
#     j = 4 : index 0 = *****
# Pattern:
# *****

# i = 1
#     j = 0 : index 0 = *
#     j = 1 : index 0 = **
#     j = 2 : index 0 = ***
#     j = 3 : index 0 = ****
# Pattern:
# *****
# ****

# i = 2
#     j = 0 : index 0 = *
#     j = 1 : index 0 = **
#     j = 2 : index 0 = ***
# Pattern:
# *****
# ****
# ***

# i = 3
#     j = 0 : index 0 = *
#     j = 1 : index 0 = **
# Pattern:
# *****
# ****
# ***
# **

# i = 4
#     j = 0 : index 0 = *
# Pattern:
# *****
# ****
# ***
# **
# *
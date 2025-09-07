# *
# * *
# * * *
# * * * *
# * * * * *

def Pattern():
    n = int(input("Enter number of rows: "))
# For Rows
    for i in range(n):
        # For Column
        for j in range(i + 1): 
            print("*", end=" ")
        print()
Pattern()


# ---------------------------------Trace-------------------------------------:
# if n = 5
# i = 0(row) =True :
#     J = 0:  Index 0 = *
# Pattern:
# *

# i = 1(row) =True :
#     J = 0: Index 0 = *
#     J = 1: Index 1 = **
# Pattern:
# *
# **

# i = 2(row) =True :
#     J = 0: Index 0 = *
#     J = 1: Index 1 = **
#     J = 2: Index 2 = ***

# Pattern:
# *
# **
# ***

# i = 3(row) =True :
#     J = 0: Index 0 = *
#     J = 1: Index 1 = **
#     J = 2: Index 2 = **
#     J = 3: Index 3 = ***
# Pattern:
# *
# **
# ***
# ****

# i = 4(row) =True :
#     J = 0: Index 0 = *
#     J = 1: Index 1 = **
#     J = 2: Index 2 = ***
#     J = 3: Index 3 = ****
#     J = 4: Index 4 = *****
# Pattern:
# *
# **
# ***
# ****
# *****

# 1
# 12
# 123
# 1234
# 12345

def Pattern():
    n = int(input("Enter number of rows: "))
    for i in range(1, n + 1):             
        for j in range(1, i + 1):
            print(j, end= " ")
        print()
Pattern()

# ---------------------------------Trace-------------------------------------:
# if n = 5:

# i = 1 (Row ): True
#     j = 1 : Index 0 = 1
# Pattern:
# 1

# i = 2 (Row ): True
#     j = 1 : Index 0 = 1
#     j = 2 : Index 1 = 12
# Pattern:
# 1
# 12

# i = 3 (Row ): True
#     j = 1 : Index 0 = 1
#     j = 2 : Index 1 = 12
#     j = 3 : Index 2 = 123
# Pattern:
# 1
# 12
# 123

# i = 4 (Row ): True
#     j = 1 : Index 0 = 1
#     j = 2 : Index 1 = 12
#     j = 3 : Index 2 = 123
#     j = 4 : Index 3 = 1234
# Pattern:
# 1
# 12
# 123
# 1234

# i = 5 (Row ): True
#     j = 1 : Index 0 = 1
#     j = 2 : Index 1 = 12
#     j = 3 : Index 2 = 123
#     j = 4 : Index 3 = 1234
#     j = 5 : Index 4 = 12345
# Pattern:
# 1
# 12
# 123
# 1234
# 12345
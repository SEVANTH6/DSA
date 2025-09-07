# 12345
# 1234
# 123
# 12
# 1

def Pattern():
    n = int(input("Enter Number of Rows: "))

    for i in range(n): 
        for j in range(1, n - i + 1): 
            print(j, end= " ")
        print()

Pattern()


# ---------------------------------Trace-------------------------------------:
# if n = 5:

# i = 0
    # j = 1: Index 0 = 1
    # j = 2: Index 0 = 12
    # j = 3: Index 0 = 123
    # j = 4: Index 0 = 1234
    # j = 5: Index 0 = 12345
# Pattern:
# 12345

# i = 1
    # j = 1: Index 0 = 1
    # j = 2: Index 0 = 12
    # j = 3: Index 0 = 123
    # j = 4: Index 0 = 1234
# Pattern:
# 12345
# 1234

# i = 2
    # j = 1: Index 0 = 1
    # j = 2: Index 0 = 12
    # j = 3: Index 0 = 123
# Pattern:
# 12345
# 1234
# 123

# i = 3
    # j = 1: Index 0 = 1
    # j = 2: Index 0 = 12
# Pattern:
# 12345
# 1234
# 123
# 12

# i = 4
    # j = 1: Index 0 = 1
# Pattern:
# 12345
# 1234
# 123
# 12
# 1
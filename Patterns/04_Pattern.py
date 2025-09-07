# 1
# 22
# 333
# 4444
# 55555

def Pattern():
    n = int(input("Enter number of rows: "))

    # Rows
    for i in range(1, n + 1):
        #Column
        for j in range(1, i + 1):
            print(i, end= " ")
        print()
Pattern()    

# ---------------------------------Trace-------------------------------------:
# if n = 5:

# i = 1(Row): (True)
#   j = 1: Index 0 = 1
# Pattern:
# 1

# i = 2(Row): (True)
#   j = 1: Index 0 = 2
#   j = 2: Index 1 = 22
# Pattern:
# 1
# 22

# i = 3(Row): (True)
#   j = 1: Index 0 = 3
#   j = 2: Index 1 = 33
#   j = 3: Index 2 = 333
# Pattern:
# 1
# 22
# 333


# i = 4(Row): (True)
#   j = 1: Index 0 = 4
#   j = 2: Index 1 = 44
#   j = 3: Index 2 = 444
#   j = 4: Index 3 = 4444
# Pattern:
# 1
# 22
# 333
# 4444

# i = 5(Row): (True)
#   j = 1: Index 0 = 5
#   j = 2: Index 1 = 55
#   j = 3: Index 2 = 555
#   j = 4: Index 3 = 5555
#   j = 5: Index 4 = 55555
# Pattern:
# 1
# 22
# 333
# 4444
# 55555

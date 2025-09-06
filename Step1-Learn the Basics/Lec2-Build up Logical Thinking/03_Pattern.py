# 1
# 12
# 123
# 1234
# 12345

def Pattern():
    for i in range(1, 6):             
        for j in range(1, i + 1):
            print(j, end= " ")
        print()
Pattern()
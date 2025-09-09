# Factorial

number = int(input("Enter the Number: "))
fact = 1

for i in range(1, number + 1):
    fact = fact * i 

print(fact)


# Trace of Execution:

# if Number = 4:
#      i = 1: 
#          fact = fact * i 
#          1 = 1 * 1 = 1
#      i = 2: 
#          fact = fact * i 
#          1 = 1 * 2 = 2
#     i = 3: 
#          fact = fact * i 
#          2 = 2 * 3 = 6
#     i = 4: 
#          fact = fact * i 
#          6 = 6 * 4 = 24

# Output: 24
     
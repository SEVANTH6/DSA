#  Swappping Two Numbers

A = int(input("Enter First Number: "))
B = int(input("Enter Second Number: "))

print(f"Before Swapping A is: {A} and B is: {B}")

# Method 1:
# A, B = B, A

# Method 2:
A = A + B
B = A - B
A = A - B

print(f"After Swapping A is: {A} and B is: {B}")


# Trace of Execution:       
# A = 5
# B = 10

# Before Swapping A is: 5 and B is: 10
#using method 1:
# A, B = B, A
# 10, 5 = 5, 10
# After Swapping A is: 10 and B is: 5

# using method 2:
# A = A + B : 10 = 10 + 5 => 15(A) 
# B = A - B : 5 = 15 - 10 => 5(B)
# A = A - B : 10 = 15 - 5 => 10(A)
# After Swapping A is: 10 and B is: 5
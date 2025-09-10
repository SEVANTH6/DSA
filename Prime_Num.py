#  Prime Number 

num = int(input("Enter a Nuber: "))

if num > 1:
    for i in range(2, num):   # check from 2 to num-1  
        if num % i == 0:  # if num is divisible by any number other than 1 and itself
            print(f"{num} not a prime Number")
            break
    else:
        print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")



# Trace of Execution:

# if num = 7:
#   i = 2: 7 % 2 = 1 (not 0)
#   i = 3: 7 % 3 = 1 (not 0)
#   i = 4: 7 % 4 = 3 (not 0)
#   i = 5: 7 % 5 = 2 (not 0)
#   i = 6: 7 % 6 = 1 (not 0)
#   No divisors found  
# output: '7 is a Prime Number'

# if num = 8:
#   i = 2: 8 % 2 = 0 (divisor found)
#   Output: '8 not a prime Number'

# if num = 2:
#   No loop runs (range(2,2) is empty)
#   Output: '2 is a Prime Number'

# if num = 1:
#   Output: '1 is not a Prime Number'
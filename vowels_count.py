# Vowels_counting 

vowels = ["a", "e", "i", "o", "u"]
count = 0    

string = input("Enter a String: ").lower() 

for char in string: 
    if char in vowels: # in operator checks if the character is in the vowels list
        count += 1 

print(f"Number of Vowels in the {string} is: {count}")


# Trace of Execution:

# string = "Sevanth"
# first for loop iterate in each char of the string
# then:
# check char = 's' in vowels = False
# Count = 0
# check char = 'e' in vowels = True
# Count = 1
# check char = 'v' in vowels  = False
# Count = 1
# check char = 'a' in vowels  = True
# Count = 2
# check char = 'n' in vowels  = False
# Count = 2
# check char = 't' in vowels  = False
# Count = 2
# check char = 'h' in vowels  = False
# Count = 2

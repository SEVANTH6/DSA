# Counts the occurance of each character in a given string

string1 = input("Enter a Word: ").upper()

dict1 = {}   #For key,value

for char in string1:  
    if char not in dict1: 
        dict1[char] = 1 
    else:
        dict1[char] += 1

print(dict1)


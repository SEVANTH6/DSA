# Palindrome Check Program 

str = input("Enter a String: ")
reversed_str = ""  # for Stroring reversed Characters.

for character in str: # for each character in the string
    reversed_str = character + reversed_str  #storing characters in reverse order.

if reversed_str == str: #Compares the original string with the reversed string.
    print("Its a Palindrome")
else:
    print("Its Not a palindrome")



# Trace of Execution:

# input = "madam"
# reversed_str = ""
# Loop:
#   character = 'm' -> reversed_str = 'm'
#   character = 'a' -> reversed_str = 'a' + 'm' = 'am'
#   character = 'd' -> reversed_str = 'd' + 'am' = 'dam'
#   character = 'a' -> reversed_str = 'a' + 'dam' = 'adam'
#   character = 'm' -> reversed_str = 'm' + 'adam' = 'madam'
# reversed_str = "madam"
# Compare: "madam" == "madam" -> True
# Output: Its a Palindrome

# input = "hello"
# reversed_str = ""
# Loop:
#   character = 'h' -> reversed_str = 'h'
#   character = 'e' -> reversed_str = 'e' + 'h' = 'eh'
#   character = 'l' -> reversed_str = 'l' + 'eh' = 'leh'
#   character = 'l' -> reversed_str = 'l' + 'leh' = 'lleh'
#   character = 'o' -> reversed_str = 'o' + 'lleh' = 'olleh'
# reversed_str = "olleh"
# Compare: "hello" == "olleh" -> False
# Output: Its Not a palindrome




# A program to calculate the length of a string.
string_length = "Vivina Oliveros "
length = len(string_length)
print("Length of the string:", length)

# A program to count the number of characters in a string.
character_count = "Barbanida"
count = sum(1 for char in character_count)
print("Number of characters:", count)

# A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change(string):
    first = string[0]
    return first + string[1:].replace(first, '$')

string = "aghakad"
result = change(string)
print("Changed String:", result) 

# A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

swapped = swap("Vivina", "Oliveros")
print("Swapped string:", swapped)

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
var1 = "My"
var2 = "name"
var3 = "is"
var4 = "Vivina"
concatenated = var1 + " " + var2 + " " + var3 + " " + var4
print("Concatenated string:", concatenated)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
concatenated = string1 + " " + string2
print("Concatenated input:", concatenated)

# Using + Concatenate in Python using your name and your age in a paragraph
name = "Vivina"
age = 22
paragraph = "My name is " + name + " and I am " + str(age) + " years old."
print(paragraph)
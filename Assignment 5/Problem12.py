# 12. Write a Python function to convert a given string to all uppercase if it contains at 
# least 2 uppercase characters in the first 4 characters.

def Convert_to_uppercase(str):
    n = 0
    for letter in str[:4]: 
        if letter.upper() == letter:
            n += 1
    if n >= 2:
        return str.upper()
    return str

print(Convert_to_uppercase('Mango'))
print(Convert_to_uppercase('ManGo'))

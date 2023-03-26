# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 

def string_reverse(str):
    if len(str) % 4 == 0:
       return ''.join(reversed(str))
    return str

print(string_reverse('Python'))
print(string_reverse('Boarding'))
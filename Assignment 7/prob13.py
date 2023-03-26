# 13. Write a Python program to remove duplicates from Dictionary.

my_dict = {'x':500, 'y':5874, 'z': 560, 'x':500, 'a':1500}
result = {}

for key,value in my_dict.items():
    if value not in result.values():
        result[key] = value

print(result)

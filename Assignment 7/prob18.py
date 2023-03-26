# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
# #

my_list = [{},{},{}]
my_list1 = [{1:2},{},{}]
print(all(not d for d in my_list))
print(all(not d for d in my_list1))

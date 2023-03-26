# 20. Write a Python program to remove all consecutive duplicates of a given string.

from itertools import groupby 
def remove_all_consecutive(str): 
	result_str = [] 
	for (key,group) in groupby(str): 
		result_str.append(key) 

	return ''.join(result_str)
	
str = 'aaabbccdddddfff'
print("Original string:" + str)
print("After removing consecutive duplicates: " + str)
print(remove_all_consecutive(str))
# 7. Write a Python program that counts the number of elements within a list that are greater 
# than 30.


def count_range(li, num):
	count = 0
	for x in li:
		if  x > num:
			count += 1
	return count

list1 = [10,20,30,40,60,70,70,80,99]
print(count_range(list1, 30))



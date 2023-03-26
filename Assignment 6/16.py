# 16. Take inputs from user to make a list. Again take one input from user and 
# search it in the list and delete that element, if found. Iterate over list using for loop.


print(end="Enter the Size of List: ")
size = int(input())

lst = []
print(end="Enter " +str(size)+ " Elements: ")
for i in range(size):
    lst.append(input())

print(end="\nEnter the Value to Delete: ")
val = input()

if val in lst:
    lst.remove(val)
    print("\nThe New list is: ")
    for i in range(size-1):
        print(end=lst[i]+" ")
else:
    print("\nElement doesn't exist in the List!")

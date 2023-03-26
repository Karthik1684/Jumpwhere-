# 20.You are given with a list of integer elements. Make a new list which will store
#  square of elements of previous list.


num = [1,2,3,4]
squares = []
for i in num:
    squares.append(i**2)

print("The given list is:",num)
print("The squares of given list:",squares)
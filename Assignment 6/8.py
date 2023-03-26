# 8. Take values of length and breadth of a rectangle from user and check if it is square or not.

length  = int(input("Enter the length  of a rectangle:"))
breadth = int(input("Enter the breadth of a rectangle:"))
if length == breadth:
    print("The entered rectangle is a square.")
else:
    print("Area = ",length*breadth)
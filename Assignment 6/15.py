# 15. Take integer inputs from user until he/she presses q 
# ( Ask to press q to quit after every integer input ). Print average and product of all numbers.


print("Start entering numbers")
sum = 0
count = 0
while 1:
    num = int(input())
    count = count+1
    sum = sum+num
    print("Press q when you are done inputting the numbers or y to continue")
    m = input()
    if m=='q':
        break
    
print("Average",sum/count)
print("Sum",sum)

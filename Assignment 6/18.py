# 18. From the two list obtained in previous question, make new lists, containing only
#  numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
even = []
odd = []
four = []
six = []
eight = []
ten = []
three = []
five = []
seven = []
nine = []

for i in range(1,101):
    if(i%2 == 0):
        even.append(i)
    else:
        odd.append(i)

for i in even:
    if i%4 == 0:
        four.append(i)
    if i%6 == 0:
        six.append(i)
    if i%8 == 0:
        eight.append(i)
    if i%10 == 0:
        ten.append(i)

for i in odd:
    if i%3 == 0:
        three.append(i)
    if i%5 == 0:
        five.append(i)
    if i%7 == 0:
        seven.append(i)
    if i%9 == 0:
        nine.append(i)

print("Numbers divisible by 4:",four)
print("Numbers divisible by 6:",six)
print("Numbers divisible by 8:",eight)
print("Numbers divisible by 10:",ten)
print("Numbers divisible by 3:",three)
print("Numbers divisible by 5:",five)
print("Numbers divisible by 7:",seven)
print("Numbers divisible by 9:",nine)
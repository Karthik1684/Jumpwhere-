# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


noh = input("Number of classes held")
noa = input("Number of classes attended")
attendence = (noa/float(noh))*100
print("Attendence is",attendence) 
if attendence >= 75:
  print("You are allowed to sit in exam") 
else:
  print("Sorry, you are not allowed. Attend more classes from next time.") 
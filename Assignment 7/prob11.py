# 11. Write a Python program to sort a dictionary by key.

myDict = { 'a':1,
           'b':2,
           'c':3,
           'd':4 }

for key in sorted(myDict):
    print("%s: %s" % (key, myDict[key]))
	
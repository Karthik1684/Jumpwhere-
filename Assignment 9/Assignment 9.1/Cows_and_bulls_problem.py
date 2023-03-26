# Assignment 9.1 - Cows and bulls problem

#		 Create a program that will play the “cows and bulls” game with the user. The game works like this:

#		 Randomly generate a 4-digit number. Ask the user to guess a 4-digit number(Digits should not be repeated). For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

#		 Say the number generated by the computer is 1038. An example interaction could look like this:

#		   Welcome to the Cows and Bulls Game! 
#		   Enter a number: 
#		   >>> 1234
#		   2 cows, 0 bulls
#		   >>> 1250
#		   1 cow, 1 bull
#		   ...
#		 Until the user guesses the number.


import random

def getDigits(num):
	return [int(i) for i in str(num)]
	
def noDuplicates(num):
	num_li = getDigits(num)
	if len(num_li) == len(set(num_li)):
		return True
	else:
		return False
	
def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicates(num):
			return num

def numOfBullsCows(num,guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)
	
	for i,j in zip(num_li,guess_li):
		
		if j in num_li:
		
			if j == i:
				bull_cow[0] += 1
			else:
				bull_cow[1] += 1
				
	return bull_cow

num = generateNum()
tries =1

while 1:
	guess = int(input("Enter your guess: "))
	
	if not noDuplicates(guess):
		print("Number should not have repeated digits. Try again.")
		continue
	if guess < 1000 or guess > 9999:
		print("Enter 4 digit number only. Try again.")
		continue
	
	bull_cow = numOfBullsCows(num,guess)
	print(f"{bull_cow[0]} cows, {bull_cow[1]} bulls")
	tries +=1
	
	if bull_cow[0] == 4:
		print("You guessed right!")
		break
print("Total number of guesses made :",tries)

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

number = 20

while True:
	if number % 17 != 0:
		number += 1
		continue
		
	found = True
	
	for x in range(1, 21):
		if number % x != 0:
			found = False
			break
	
	if found:
		break
		
	number += 1

print(number)

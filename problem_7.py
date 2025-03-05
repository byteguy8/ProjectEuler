# What is the 10001 st prime number?

st = 8
last = None
counter = 2

while True:
	if counter % 2 == 0 or counter % 3 == 0 or counter % 5 == 0 or counter % 7 == 0:
		counter += 1
		continue
	if counter % 11 == 0 or counter % 13 == 0 or counter % 17 == 0 or counter % 23 == 0:
		counter += 1
		continue
	
	prime = True
	divisors = 0
	
	for x in range(1, counter + 1):
		if counter % x == 0:
			divisors += 1

		if divisors > 2:
			prime = False
			break

	if prime:
		st += 1
		last = counter
		
	if st == 10001:
		break

	counter += 1

print(last)

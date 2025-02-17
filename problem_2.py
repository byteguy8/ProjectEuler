# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 2
c = 0
sum = 2
limit = 4000000

while c < limit:
	c = a + b
	
	if c % 2 == 0:
		sum += c
	
	a = b
	b = c

print(sum)

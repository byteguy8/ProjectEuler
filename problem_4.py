# Find the largest palindrome made from the product of two 3-digit numbers.

a = 100
b = 100
largest = 0

while b < 1000:
	c = a * b
	cstr = str(c)
	rcstr = cstr[::-1]
	
	if cstr == rcstr and c > largest:
		largest = c
		
	a += 1
	
	if a == 1000:
		a = b + 1
		b += 1
	
print(largest)

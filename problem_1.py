# Find the sum of all the multiples 3 or 5 below 1000

start = 3
end = 1000
sum = 0

for x in range(start, end):
	if x % 3 == 0 or x % 5 == 0:
		sum += x
		
print(sum)

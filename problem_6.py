# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sum = 0
sum_sq = 0

for x in range(1, 101):
    sum += x
    sum_sq += x * x

print(sum * sum - sum_sq)

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

array = range(1,100)
factors = []


for num in array:
	if num % 3 == 0:
		factors.append(num)
	elif num % 5 == 0:
		factors.append(num)

sum_of_factors = sum(factors)
print sum_of_factors

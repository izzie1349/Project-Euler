# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

list_of_numbers = range(1, 10)
list_of_primes = []

for num in list_of_numbers:
    if (num % 1 == 0) and (num % num == 0):
        list_of_primes.append(num)

print list_of_primes

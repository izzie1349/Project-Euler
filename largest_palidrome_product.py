#!/usr/bin/env python
#coding: utf8

"""

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

# list of all 3 digit numbers
three_digit_num = range(100,1000)
products = []


for x in three_digit_num:
	for y in three_digit_num:
		prod = x*y

		if str(prod) == str(prod)[::-1]:
			products.append(prod)

print max(products)






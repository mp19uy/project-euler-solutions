# Here's a list of algorithms to factor numbers: 
# https://en.wikipedia.org/wiki/Integer_factorization#Factoring_algorithms
# 
# Solution #1 - uses trial division
import math

n = 600851475143
i = 2

while i*i < n:
	while n % i == 0:
		n = n / i
	i=i+1

print(n)
#Solution #1 it's pretty basic just goes over the whole fibonacci sequence and
# check if the number is odd, if it's: sum it to the counter

#Solution #2 takes advantage of a property of the sequence:
# https://en.wikipedia.org/wiki/Fibonacci_number#Primes_and_divisibility
# Every 3rd number of the sequence is even, so there is no need to do
# an odd check because we know exactly how the odd numbers are distributed
# along the fibonacci sequence

#Solution 1:
fib_ant = 0
fib = 1
sum = 0
while fib <= 4000000:
	if (fib % 2) == 0:
		sum=sum + fib
	tmp = fib
	fib = fib + fib_ant
	fib_ant = tmp
print(sum)

#Solution 2:
fib_ant = 1
fib = 2
sum = 0

while fib <= 4000000:
	sum=sum + fib
	for i in (0,1,2):
		tmp = fib
		fib = fib + fib_ant
		fib_ant = tmp
print(sum)

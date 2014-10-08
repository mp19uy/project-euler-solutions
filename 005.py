#This solution takes a part from 003.py

merge_primes = {"2" : 0,"3" : 0,"5" : 0,"7" : 0,"11" : 0,"13" : 0,"17" : 0,"19" : 0}
local_primes = {"2" : 0,"3" : 0,"5" : 0,"7" : 0,"11" : 0,"13" : 0,"17" : 0,"19" : 0}

#Find the descomposition of n
n = 20

while n > 1:
	j = 2
	k = n
	while j <= k:
		while k % j == 0:
			local_primes[str(j)] = local_primes[str(j)] + 1
			k = k / j
		j=j+1
	n = n - 1
	for key, value in merge_primes.items():
		if (local_primes[key] > value):
			merge_primes[key]=local_primes[key]
		local_primes[key] = 0

smallest = 1

for key, value in merge_primes.items():
	smallest = smallest * (int(key)**merge_primes[key])
print(smallest)

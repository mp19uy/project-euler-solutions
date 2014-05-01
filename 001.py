#Solutions #1 and #2 are using both
# the principle of inclusion-exclusion
#Solutions #2 takes advantage of an equality of sumatories
#Solution #3 check the divisibility between 3 or 5
#And add it to the counter if it passes the check

#Solution 1:
sum = 0
i = 3
while i < 1000:
    sum=sum+i
    i+=3

i = 5
while i < 1000:
    sum=sum+i
    i+=5

i = 15
while i < 1000:
    sum=sum-i
    i+=15

print(sum)

#Solution 2:
sum = 0
max3 = 999//3
max5 = 999//5
max15 = 999//15
# sum of i from 1 to n is equal to (n)*(n+1)/2
sum = 3*(max3)*(max3+1)//2 + 5*(max5)*(max5+1)//2 - 15*(max15)*(max15+1)//2
print(sum)

#Solution 3:
sum = 0
for i in range(1,1000):
    if (i%3)==0 or (i%5)==0:
        sum=sum+i
print (sum)
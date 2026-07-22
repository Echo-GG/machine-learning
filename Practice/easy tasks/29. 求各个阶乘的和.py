def Fact(n):
    if n == 0 or n==1:
        return 1
    return n*Fact(n-1)
sum = 0
for i in range(1,21):
    sum += Fact(i)
print(sum)

# Another solution:
import math
sum = 0
for i in range(1,21):
    sum += math.factorial(i)
print(sum)
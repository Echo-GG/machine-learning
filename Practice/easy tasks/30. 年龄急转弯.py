first = 10
second = first + 2
third = second + 2
fourth = third + 2
fifth = fourth + 2
print(fifth)

# Another solution:
# Recursive solution:
def func(n):
    if n == 1:
        return 10
    else:
        return func(n-1) + 2
print(func(5))
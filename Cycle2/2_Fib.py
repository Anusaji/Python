from math import sqrt

def fib(n):

    return int(((((pow((1 + sqrt(5)), n)))-((pow((1 - sqrt(5)), n))))/((pow(2, n))*(sqrt(5)))))

# Driver Code

for i in range(6):

    print(fib(i), end=" ")

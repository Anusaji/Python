def factorCheck(n):

    # Method 1

    # factors = []

    # for i in range(1, n+1):

    #     if n % i == 0:

    #         factors.append(i)

    # return factors

    # Method 2

    return [x for x in range(1, n+1) if n % x == 0]

n = int(input("Enter a number :"))

print(factorCheck(n))
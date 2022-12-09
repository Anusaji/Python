def longest(l):

    return sorted(l, key=len)[-1]

s = input("Enter list of Words :").split()

print(longest(s))
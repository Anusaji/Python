def occurance(s):

    d = {}

    for i in set(s):

        d[i] = s.count(i)

    return d

s = input("Enter the String :")

print(occurance(s))
def ing(s):

    if s[-3::] == "ing":

        res = s[:-3:] + "ly"

        return res

    else:

        s += "ing"

        return s

s = input("Enter a word :")

print(ing(s))
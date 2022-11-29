a=[int(value) for value in input("enter the first list").split()]
b=[int(value) for value in input("enter the second list").split()]
print("whether strings are of same length:",len(a)==len(b))
print(f"is sum of list a = sum of list b:{sum(a)==sum(b)}")
print([x for x in a if x in b],"are the common elements")

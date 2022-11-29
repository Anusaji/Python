d={'key1':'value1','key2':'value2'}
print(d)
car={'company':'bmw','model':'m3'}
print(car['model'])
print(car)
car['year']=2000
car['color']=['red','blue']
print(car.get('color'))
print(car.values())



dict1={}
n=int(input("enter number of items for the dictionary"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dict1[key]=value
print(dict1)


#merge using update function
dict1={}
n=int(input("enter number of items for the first dictionary"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dict1[key]=value
print(dict1)
dict2={}
n=int(input("enter number of items for the dictionary"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    dict2[key]=value
print(dict2)
print("after merging")
dict1.update(dict2)
print(dict1)


#merging
d1={}
n=int(input("enter number of items for the first dictionary"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    d1[key]=value
print(d1)
d2={}
n=int(input("enter number of items for the dictionary"))
for i in range(n):
    key=input("enter key")
    value=input("enter value")
    d2[key]=value
print(d2)
d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
        d3[k]=[v,d1[k]]
print(d3)

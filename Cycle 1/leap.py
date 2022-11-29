a=int(input("enter starting year"))
b=int(input("enter ending year"))
for i in range(a,b):
    if(i%400==0 and i%100==0):
        print(i)
    elif(i%4==0 and i%100!=0):
        print(i)
    else:
        print(i,"is not a leap year")

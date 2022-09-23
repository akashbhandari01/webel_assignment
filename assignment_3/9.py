def facto(a):
    if (a==1 or a==0):
        return 1
    else:
        return a*facto(a-1)
a=int(input("Enter a Number: "))
b=facto(a)
print("The factroial of is: ",b)

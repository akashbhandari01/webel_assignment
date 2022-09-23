def number(n):
    x=0
    for i in range(n+1):
        x+=i
    return x
a=int(input("Enter The Value of N: "))
print("The Sum of first N Natural number: ",number(a))

def number(n):
    i=n
    while(i>=1):
        print(i,end=" ")
        i=i-1
a=int(input("Enter The Value N Number: "))
print("The first N natural numbers in reverse order:",end=" ")
number(a)
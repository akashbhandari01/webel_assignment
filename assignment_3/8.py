def solution(n):
    a=1
    b=0
    c=1
    while(b<n-1):
        c+=2
        a+=c
        b+=1
    return a
print("Calculation of sum of first N odd natural numbers is: ",solution(int(input("Enter The value of N: "))))
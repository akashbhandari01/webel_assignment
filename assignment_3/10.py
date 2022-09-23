num=int(input("Enter the value of N: "))
product=1
for i in range(1,num+1):
    product = product*(2*i-1)
print("The Product of first N odd number is:",product)
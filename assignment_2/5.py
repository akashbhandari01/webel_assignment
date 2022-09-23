y=int(input("Enter The Year: "))
if((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):   
    print("%d is Leap Year."%y);  
 
else:  
    print ("%d is not Leap Year."%y)  

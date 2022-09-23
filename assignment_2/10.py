marks1=int(input("Enter The Marks of First Subject: "))
marks2=int(input("Enter The Marks of Second Subject: "))
marks3=int(input("Enter The Marks of Third Subject: "))
marks4=int(input("Enter The Marks of Fourt Subject: "))
marks5=int(input("Enter The Marks of Fifth Subject: "))
marks=(marks1+marks2+marks3+marks4+marks5)/5
if(marks>=90):
    print("Student Pass.")
    print("Grade: A")
elif(marks>=80):
    print("Student Pass.")
    print("Grade: B")
elif(marks>=70):
    print("Student Pass.")
    print("Grade: C")
elif(marks>=60):
    print("Grade: D")
elif(marks>=50):
    print("Student Pass.")
    print("Grade: E")
else:
    print("Student Fail.")
    print("Gread:F")
    
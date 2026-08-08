subject1 = float(input("enter the marks of subject 1 :"))
subject2 = float(input("enter the marks of subject 2 :"))
subject3 = float(input("enter the marks of subject 3 :"))
subject4 = float(input("enter the marks of subject 4 :"))
subject5 = float(input("enter the marks of subject 5 :"))

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total/500)*100

if (percentage >= 75):
    print("Grade: Distinction")
elif (percentage >= 65):
    print("Grade: I Class")
elif (percentage >= 40):
    print("Grade: II Class")
else:
    print("Grade: Fail")

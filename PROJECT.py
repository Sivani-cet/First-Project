S=0
C=0
sub=[]
credit =[]
print ("Welcome!!")
x=int(input("How many subjects do you have?"))
for i in range (x):
    sub.append(input("Enter name of subject:"))
    credit.append(float(input("Enter credit value:")))
    n=input("Do you know your grade?")
    if n=="yes":
        t=input("What is your grade?")
        if t=="S":
            q=10
        elif t=="A+":
            q=9
        elif t=="A":
            q=8.5
        elif t=="B+":
            q=8
        elif t=="B":
            q=7.5
        elif t=="C+":
            q=7
        elif t=="C":
            q=6.5
        elif t=="D+":
            q=6
        elif t=="P":
            q=5.5
        else:
            q=0
        for j in range(x):
            S=credit[i]*q+S
            C=C+credit[i] 
        SGPA=S/C
        print ("Your SGPA value is:",SGPA)  
    else:
        a=int(input ("Enter End Semester Exam mark:"))
        b=int(input ("Enter marks obtained in first series exam:"))
        c=int(input ("Enter marks obtained in second series exam:"))
        d=int(input ("Enter Attendance in % :"))
        if d>=85:
            e=5
        elif d>=80:
            e=4
        elif d>=75:
            e=3
        elif d>=70:
            e=2
        elif d>=65:
            e=1
        else:
            e=0
        f=int(input("Enter marks obtained for assignment or microproject(15):"))    
        g=(b+c)/4
        total=a+d+f+g
        if total >=90:
            grade="S"
            q=10
        elif total >=85:
            grade="A+"
            q=9
        elif total >=80:
            grade="A"
            q=8.5
        elif total >=75:
            grade="B+"
            q=8
        elif total >=70:
            grade="B"
            q=7.5
        elif total >=65:
            grade="C+"
            q=7
        elif total >=60:
            grade="C"
            q=6.5
        elif total >=55:
            grade="D+"
            q=6
        elif total >=50:
            grade="P"
            q=5.5 
        else:
            grade="F"
            q=0
        print ("The grade you obtained in this subject is:",grade)
for i in range(x):
    S=credit[i]*q+S
    C=C+credit[i]
SGPA=S/C
print ("Your SGPA value is:",SGPA)         
              
                    
                      
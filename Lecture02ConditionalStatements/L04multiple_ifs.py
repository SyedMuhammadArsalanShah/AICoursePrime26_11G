
print("SignUP")
name=input("Enter Your Name \n")
email=input("Enter Your Email \n")
password=input("Enter Your Password \n")
contact=input("Enter Your Contact \n")

print("Account Succefully Created ")

emailLogin=input("Enter Your Email Login  \n")
passwordLogin=input("Enter Your Password Login \n")



if email == emailLogin and password==passwordLogin:

    print("welcome ", name)

    isl=float(input("Enter Your Islamiyat Marks\n"))
    urd=float(input("Enter Your Urdu Marks\n"))
    math=float(input("Enter Your Math Marks\n"))
    eng=float(input("Enter Your English Marks\n"))


    obatined_marks=isl+urd+math+eng
    per =obatined_marks/400*100



    if per <=100 and per >=80:
        print("Grade A1")
    elif per <=79 and per >=70:
        print("Grade A")
    elif per <=69 and per >=60:
        print("Grade B")
    elif per <=59 and per >=50:
        print("Grade C")
    elif per <=49 and per >=40:
        print("Grade D")
    elif per <=39 and per >=30:
        print("Iqra University Jaien")

    elif per <=29 and per >=20:
        print("Aptech Learning Men Aien ")
    else:
        print("Sir S M Arsalan Shah ke pass aien ")
        
    number=int(input("Enter Your Number"))


    if number > 0 :
        print("Positive",number)
    else:
        print("Negative", number)
     
else:
    print("incorrect email or password")
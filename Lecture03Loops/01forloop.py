

for a in range(2,20):
    print("Ramzan",a)
    
    
for a in range(3,6):
    print("Eid", a)
    
    


for a in range(20):
    
    if  a== 5:
        continue
    print(a)
    
    
for a in range(6,20):
    if a== 5:
        break
    print(a)
    
    

current =2026

birthYear= int( input("Enter Your Birth Year "))
count = 0

for  a in range(birthYear, current+1):
    
    if a%4== 0:
        count=count+1
        print("Leap Year ", a)
        
    else :
        print("Is Not A Leap Year ",a )



print("Total Leap Year ", count)
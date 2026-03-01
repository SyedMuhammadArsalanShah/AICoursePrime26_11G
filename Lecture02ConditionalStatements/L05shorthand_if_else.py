number=int(input("Enter Your Number"))

# print("even ",number) if number %2==0 else print("Odd ",number)
status="even " if number %2==0 else "Odd "
print(status,number)
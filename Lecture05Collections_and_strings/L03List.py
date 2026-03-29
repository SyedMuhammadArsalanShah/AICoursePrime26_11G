students=["Faizan", "Mahnoor", "Tehreem", "Khizer","Khizer","Khizer","Khizer", "Saad", "Shaaf"]
print(students)
print(students[0:2])
print(students[::2])


students[3]="laiba"
print(students)


students.sort()
print(students)


students.reverse()
print(students)


students.append("faham")
print(students)



students.insert(1,"ali")
print(students)



students.pop(1)
print(students)




students.remove("faham")
print(students)


print(students.count("Khizer"))

students.clear()
print(students)

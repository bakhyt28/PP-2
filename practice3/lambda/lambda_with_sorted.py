students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

sorted_students = sorted(students, key=lambda x: x[1])  # sort by age using lambda

print(sorted_students)  # print result

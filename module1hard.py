grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# grades_list = 0
#
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students_list_1 = sorted( students )
# students_list = 0
# students_list_2 = sorted( students )
# students_list = 1
# for i in grades:
#     print( students_list_1[students_list], ((sum( grades[grades_list] ) / len( grades[grades_list] ))) )
# for i in grades:
#     print( students_list_2[students_list], ((sum( grades[grades_list] ) / len( grades[grades_list] ))) )
# grades_list += 1
# students_list += 1
students = list(students)
print(students)
students_sort = sorted(students)
print(students)

grades_m = ([sum(grades[0])/len(grades[0])], [sum(grades[1])/len(grades[1])], [sum(grades[2])/len(grades[2])],
[sum(grades[3])/len(grades[3])], [sum(grades[4])/len(grades[4])])

dict1 = dict(zip(students_sort, grades_m))

print(dict1)

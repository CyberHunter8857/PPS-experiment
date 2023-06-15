
# program to calculate percentage and grade of student among 5 cources
course_1 = float(input("Enter your first course marks: "))
course_2 = float(input("Enter your second cours marks: "))
course_3 = float(input("Enter your third course marks: "))
course_4 = float(input("eEnter your fourth course marks: "))
course_5 = float(input("Enter your fifth course marks: "))
percentage = (course_1 + course_2 + course_3 + course_4 + course_5)/5
print ("your percentage is = ",percentage)
if (percentage > 75):
    print ("grade: distinction")
elif (percentage >= 60 and percentage <75):
    print ("grade: first division")
elif (percentage >= 50 and percentage <60):
    print ("grade: second division")
elif (percentage >=40 and percentage <50):
    print ("grade: third division")
else:
    print ("grade: you are fail")
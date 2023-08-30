# calculating the average height in a list

student_height = input("Input a list of student heights: ").split()
sum = 0
for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])
    sum += student_height[i]
    average = sum / len(student_height)
print(student_height)
print("Average  height for student  is {:.2f}".format(average))

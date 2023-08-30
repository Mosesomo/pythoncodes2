# programs that claculates the highest score in the list

student_score = (input("Input a list of student score: ")).split()

for n in range(len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print("The highest score in the list is {}" .format(max_score))
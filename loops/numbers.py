# Adding numbers from 1 to 100

sum = 0
for i in range(1, 101):
    print(i, end=" ")
    sum += i
print("")
print("Sum between 1 to 100 is {}".format(sum))
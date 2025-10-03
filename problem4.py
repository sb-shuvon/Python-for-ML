# programm : write a program to take integer input from user and display the grade according to the following criteria.


mark = int(input("Enter your mark: "))

if mark > 90 :
    print("A")
elif mark > 80 and mark <= 90 :
    print("B")
elif mark >=60 and mark <= 80 :
    print("C")
else:
    print("D")
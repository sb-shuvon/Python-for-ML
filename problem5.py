# program : get lepear year

year = int(input("Enter your year to check for lepear or not Lepear : "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 ==0:
#     print("Not leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")


# method 2

# if year % 400 == 0 and year % 100 == 0:
#     print ("Leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# else:
#     print("Not Leap Year")


# method 3

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not Leap year")

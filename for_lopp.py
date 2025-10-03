for i in range(100):
    print("I Love Python")

a = "Hello Python"
for latter in a:
    print(latter)

bag = ["alu", "piaj", "rosun", 5, 5.78, -6, 60]
for item in bag:
    print(item)

lst = [45, 21, 60, 2, 10, 60, 33, 60, 6, 8, 2,]

for i in lst:
    if i < 10:
        print(i)

# 3 and 5 dara divible number ber korar program

for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
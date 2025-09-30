Name = input("Insert your name: ")
Last_Name = input("Insert your last name: ")
Age = int(input("Insert your age: "))

Ages= ['baby','kit','preteen','teen','young adult','adult','senior citizen']

if (Age < 2):
    print(f"{Name} {Last_Name} is an {Ages[0]}")
elif (2 < Age < 9):
    print(f"{Name} {Last_Name} is an {Ages[1]}")
elif (9 < Age < 12):
    print(f"{Name} {Last_Name} is an {Ages[2]}")
elif (12 < Age < 18):
    print(f"{Name} {Last_Name} is an {Ages[3]}")
elif (18 < Age < 25):
    print(f"{Name} {Last_Name} is an {Ages[4]}")
elif (25 < Age < 60):
    print(f"{Name} {Last_Name} is an {Ages[5]}")
else:
    print(f"{Name} {Last_Name} is an {Ages[6]}")
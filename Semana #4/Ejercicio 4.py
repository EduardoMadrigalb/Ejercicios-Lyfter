print("Provide 3 numbers")
number1= int(input("Insert the first number: "))
number2= int(input("Insert the second number: "))
number3= int(input("Insert the third number: "))

if number1 > max(number2, number3):
    print(f"The number {number1} is the largest number")
elif number2 > max(number1,number3 ):
    print(f"The number {number2} is the largest number")
else:
    print(f"The number {number3} is the largest number")
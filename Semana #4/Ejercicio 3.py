import random
random_number= random.randint(1, 10)
secret_number= None
while secret_number!=random_number:
    secret_number= int(input("Guess the secret number from 1 to 10: ")) 
    if secret_number != random_number:
        print("You didn't find the secret number. try again!")
print(f"Your secret number is {random_number}.")

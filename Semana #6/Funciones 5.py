def counter_of_letters(text):
    uppercase= 0
    lowercase= 0

    for i in text:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
    return f"Uppercase: {uppercase} Lowercase: {lowercase}"

print(counter_of_letters("My day was good"))
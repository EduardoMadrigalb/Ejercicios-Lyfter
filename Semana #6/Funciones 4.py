
def reverse_string(my_string):
    original_string=""
    for i in range(len(my_string) -1,-1,-1):
        original_string += my_string[i]
    return original_string

print(reverse_string ("Today is thursday"))
    
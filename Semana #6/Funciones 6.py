def change_string_to_list(my_string):
    return my_string.split("-")

def sort_alphabetically(list):
    return sorted(list, key=str.lower)

def change_list_to_string(list):
    return "-".join(list)
   
def sort_string_alphabetically(string):
    list = change_string_to_list(string)
    sort_list = sort_alphabetically(list)
    sort_string = change_list_to_string(sort_list)
    return sort_string

my_phrase= ("My-day-was-good")

print (sort_string_alphabetically(my_phrase))
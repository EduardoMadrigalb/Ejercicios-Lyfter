def determine_prime_numbers(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False 
    return True

def filter_prime_number(list):
    return [n for n in list if determine_prime_numbers(n)]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime = filter_prime_number(numbers)
print(prime) 
print("Write 10 different numbers")

list = []
for i in range(10):
  numbers = int(input(f"Enter the number: {i+1} "))
  list.append(numbers)
max_number = max(list)
print(list)
print(f'The highest number was: {max_number}')
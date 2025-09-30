def show_menu(current_result):
    print()
    display_result(current_result)
    print("You can use this calculator for the following operations:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Clear result")
    print ("6. Exit")

    return input ("Select which operation you want to use: ")

def get_number():
    while True:
        try:
            return float(input("Enter the number you want to use:"))
        except ValueError:
            print("Invalid input! Please provide a valid number.")

def perform_operation(current_result, operation, number):
    try:
        if operation == "1":
            return current_result + number
        elif operation == "2":
            return current_result - number
        elif operation == "3":
            return current_result * number
        elif operation == "4":
            if number == 0:
                print("Error! You cannot divide by zero. Try again.")
                return current_result
            return current_result / number
    except OverflowError:
        print(" Error! The result is too large to display.")  
        return current_result  
    except Exception as e:
        print(f" Unexpected error: {e}")
        return current_result
    
def display_result(result):
    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {int(result)}")

def calculator():
    result = 0.0

    while True:
        Operation = show_menu(result)

        if Operation == "6":
            print ("You exit the calculator, goodbye!")
            break
        
        if Operation == "5":
            result= 0.0
            print ("Calculator has been cleared. You can begin again")
            continue

        if Operation not in ("1","2","3","4"):
            print ("Invalid option, please select a valid operation (1,6).")
            continue
        
        number= get_number()
        result= perform_operation(result, Operation, number)
        display_result(result)

calculator()
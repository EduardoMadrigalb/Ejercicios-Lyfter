outer_variable = "Inactive"

def global_variable():
    global outer_variable
    outer_variable = "Active"
    print("The device status is:", outer_variable)

global_variable()
print("Device status outside the function is:", outer_variable)
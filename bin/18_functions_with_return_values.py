"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

Here,
Case-1: How to access values outside the function
"""
print("Function with 1 return value")
print("-"*20)
# -------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to mention the value
# Step-2: Assign function-call to variables, so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to mention the value
    return name

# Step-2: Assign function-call to variables, so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

print("Function with more than 1 return value: Tuple")
print("-"*20)
# -------------

# 2 Steps we need to follow
# Step-1: use 'return' statement inside function to mention the value
# Step-2: Assign function-call to variables, so that returned value will be stored

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1: use 'return' statement inside function to mention the value
    return (name, company)

# Step-2: Assign function-call to variables, so that returned value will be stored
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
############################

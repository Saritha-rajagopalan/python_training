"""
Functions with variable arguments
1. Functions with variable positional arguments
2. Functions with variable keyword arguments
"""

print("1. Functions with variable positional arguments")
print("-"*20)
# -------------

# * -. syntax
# *a -> variable argument which takes 0 or more values
def add(*a):
    print("Received Values In Tuple:", a)

add()
add(10)
add(10, 20, 30)

print("#"*40, end="\n\n")
############################

print("2. Functions with variable keyword arguments")
print("-"*20)
# -------------

# ** -> is just syntax
# **a -> variable keyword arguments
def employee_profile(**a):
    print("Received Values In Dictionary:", a)


employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", email="a@b.com", phone="111111")

print("#"*40, end="\n\n")
############################

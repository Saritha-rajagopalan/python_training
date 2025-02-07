print("Strings PART-2")
print("Store the values")
print("-"*20)
# -------------

a = "C:\newfolder\test.py"
# \n -> replace with newline
# \t -> replace with tab space
print("Value of a=", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r -> Raw string
print("Value of b=", b, end="\n\n")

print("Convert existing string 'a' to raw format:", repr(a), end="\n\n")

print("#"*40, end="\n\n")
############################

print("Strings PART-3")
print("Store the values")
print("-"*20)
# -------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f -> format
# f -> replaces {variable_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
############################
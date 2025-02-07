"""
for-loop: Iterate any collections like string, list, tuple etc
"""

print("Iterate strings")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Value of i is:", i)

print("#"*40, end="\n\n")
############################

print("Iterate list")
print("-"*20)
# -------------

my_list = ["Java", "python", "C++"]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("Each Value:", i)

print("#"*40, end="\n\n")
############################

print("Iterate dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for key in my_dictionary: # Iterate key
    print("Key:", key)
    print("Value:", my_dictionary[key])
    
print("#"*40, end="\n\n")
############################
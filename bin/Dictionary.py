print("if block with dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration":10, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['duration', 'course', 'mode']
# >>>
if "duration" in my_dictionary.keys():
    print("Key 'duration' found")

# >>> my_dictionary.values()
# [10, 'python', 'online']
# >>>
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('duration', 10), ('course', 'python'), ('mode', 'online')]
# >>>
if ('duration', 10) in my_dictionary.items():
    print("Item ('duration', 10) Found")


print("#"*40, end="\n\n")
############################
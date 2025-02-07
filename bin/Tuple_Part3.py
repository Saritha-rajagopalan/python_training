print("Tuple PART-3")
print("METHODS present in 'tuple' class")
print("-"*20)
# -------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
############################

print("Tuple PART-4")
print("count and index method")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python") # 1
index_of_python = my_tuple.index("python") # 2

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("#"*40, end="\n\n")
############################
"""
In this program, we are making use of
- variables
- functions
- classes
defined in mymodule library
"""

print("1-WAY: using 'import' statement")
print("-"*20)
# -------------

import mymodule

print("Course:", mymodule.course)

add_result = mymodule.add(10,20)
print("add_result:", add_result)

e1 = mymodule.Employee()
e1.store_name("emp-1")
print("Employee 1 Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("2-WAY: using 'from-import' statement")
print("-"*20)
# -------------

from mymodule import course, add, Employee

print("Course:", course)

add_result = add(10,20)
print("add_result:", add_result)

e1 = Employee()
e1.store_name("emp-1")
print("Employee 1 Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("1-WAY: using 'import' statement with short name")
print("-"*20)
# -------------

import mypackage.db.mymodule as mm

print("Course:", mm.course)

add_result = mm.add(10,20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.store_name("emp-1")
print("Employee 1 Name:", e1.get_name())

print("#"*40, end="\n\n")
############################

print("2-WAY: using 'from-import' statement with short name")
print("-"*20)
# -------------

from mymodule import course as c, add as a, Employee as E

print("Course:", c)

add_result = a(10,20)
print("add_result:", add_result)

e1 = E()
e1.store_name("emp-1")
print("Employee 1 Name:", e1.get_name())

print("#"*40, end="\n\n")
############################
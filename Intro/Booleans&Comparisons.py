"""Use first letter as Caps for True & False """

a = True
b = False

age = 20
under_age = age < 18
print(under_age)
over_age = age >= 18
print(over_age)
"""Use double = for comparison"""
correct_age = age == 20
print("Correct Age " + str(correct_age))

"""
True & True is True
True & False is False
False & True is False
False & False is False
True or True is True
True or False is True
False or True is True
False or False is False
not True is False
not False is True
"""
print(a & a)
print(a & b)
print(b & a)
print(b & b)
print(a or a)
print(a or b)
print(b or a)
print(b or b)
print(not a)
print(not b)

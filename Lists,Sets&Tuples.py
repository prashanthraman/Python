""""
Lists hold multiple values. Represented with [].
Tuples hold multiple values. Represented with ().
Sets also hold multiple values. Represented with {}.
"""
my_list_variable = ['Hi', 'Hello', 'Howdy']
my_tuple_variable = ('Hi', 'Hello', 'Howdy')
my_set_variable = {'Hi', 'Hello', 'Howdy'}

print(my_list_variable)
print(my_tuple_variable)
print(my_set_variable)

short_tuple_variable = ('Hello',)
another_short_tuple_variable = 'Hello',

print(my_list_variable[0])
print(my_tuple_variable[0])
#print(my_tuple_variable[0]) Cannot do this as in sets elements are not stored in order

#lists has many methods under it
my_list_variable.append("Wazzup")
print(my_list_variable)

#tuples has only count & index methods under it
my_tuple_variable.count(1)
print(my_tuple_variable)

#Elements cannot be appended to tuples directly. To append need to do add another tuple as below
my_tuple_variable = my_tuple_variable + ("Wazzup",)
print(my_tuple_variable)

#Sets dont allow duplicate values
my_set_variable.add("Hello")
print(my_set_variable)
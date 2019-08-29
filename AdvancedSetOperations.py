set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9}

""""
Intersection takes common elements between 2 sets
"""
print(set_one.intersection(set_two))
print(set_one & set_two)
""""
Union takes all elements from both sets and removes duplicates
"""
print(set_one.union(set_two))
print(set_one | set_two)
""""
Difference removes elements from set 1 which is common in set 2
"""
print(set_one.difference(set_two))
print(set_one - set_two)

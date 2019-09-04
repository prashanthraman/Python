"""Key value pairs. Rules of set like no duplicates and no order of storage applies to keys of dictionaries"""
friends = {'ABC': 6,
           'DEF': 12,
           'GHI': 50}

print(friends)

# Dictionaries can hold any type of values
friends = {'ABC': 6,
           'DEF': {'WE': 'GHY'},
           'GHI': [50, 57]}

print(friends)

players=[{'name':'John',
          'numbers':(50,20,10,5,3)},
         {'name': 'Reese',
          'numbers': (20, 10, 4, 2, 3)}
         ]

player_one=players[0]
print(player_one['name'])

print(sum(player_one['numbers']))
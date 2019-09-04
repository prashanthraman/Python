numbers = list(range(10))
print(numbers)

double_numbers = [n * 2 for n in numbers]
print(double_numbers)
# Above ceomprehension is equal to below expansion
for num in numbers:
    double_numbers.append(num * 2)

print(double_numbers)

# List Comprehension of strings
age = [f'I am {num} years old.' for num in double_numbers]
print(age)

#Another lower case example.
names_list=['John','Root']
lower_case=[name.lower() for name in names_list]
print(lower_case)

friends=['root','ruth','Anne']
guests=['Root','Jose','Charlie','anne']

#if want to pick common from both and capitalise first letter
common=[name.capitalize() for name in guests if name.capitalize() in friends]
print(common)
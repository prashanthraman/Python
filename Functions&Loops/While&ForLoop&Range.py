i = 0

while i < 10:
    print(f"{i} Iteration")
    i += 1

primes = [2, 3, 5, 7, 11]
for prime in primes:
    print(prime)

for i in range(10):
    print(i)

dict1={'Jose':6,
       'Rolf':12,
       'Anne':5}

#To iterate over dictionary do as below
#Below is also called tuple deconstruction
for name,days in dict1.items():
    print(f"I saw {name} {days} days ago.")

know='Rolf'
if know in  dict1:
    print(f"I know {know}")
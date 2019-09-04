car_production = ['ok', 'ok', 'ok', 'faulty', 'ok']

# Continue keyword skips the current iteration
for car_status in car_production:
    if car_status == 'faulty':
        continue
    else:
        print(f"Car production status is {car_status}")

print("Entering break loop")
# break keyword exits out of the loop
for car_status in car_production:
    if car_status == 'faulty':
        break
    else:
        print(f"Car production status is {car_status}")

print("Generating prime")
stop = int(input("Enter the number till which you want to generate the prime numbers: "))
for n in range(2, stop):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} is equal to {x} * {n // x}")
            break
    else:
        print(f"{n} is a prime number.")

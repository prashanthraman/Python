def greet():
    name=input("Enter your name: ")
    print(f"Hello, {name}")

greet()

#Parameter is the receiving end while argument is the giving end
def check_if_prime(n):#Parameter
    for x in range(2,n):
        if n%x==0:
            print(f'{n} is equal to {x} * {n}//{x}')
    else:
        print(f"{n} is a prime number")

check_if_prime(17)#Argument

def i_return():
    return 5+5

def i_print():
    print(5+5)

result=i_return()
result1=i_print()

print(f"Return value is:{result}")
print(f"Return value is:{result1}")
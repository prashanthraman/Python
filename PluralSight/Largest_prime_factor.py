def factor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    print(n)


factor(600851475143)

programmer = True

if programmer:
    print("Inside if")
else:
    print("Inside else")

if not programmer:
    print("Inside if")
elif programmer:
    print("Inside elif")
else:
    print("Inside else")
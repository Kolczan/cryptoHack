def modular_arithmetic_2():
    a = pow(3,17)
    b = 17
    c = a % b
    x = pow(5,17)
    y = 17
    z = x % y

    s = pow(7,16)%17
    print("First number is: " + str(c) + ", second number is: " + str(z))
    print(s)
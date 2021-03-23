x = int(input("Check for a prime: "))
for i in range(round(x / 2)):
    if (i != 0):
        if (x % (i+1) == 0):
            print("Not a prime number")
            break
        elif (i+1 == round(x/2)):
            print("{} is a prime number".format(x))
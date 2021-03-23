x = int(input("Check for a prime: "))
for i in range(x / 2):
    if (x % i+1 == 0):
        print("not a prime")
        break
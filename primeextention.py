def checkprime():
    x = int(input("Check for a prime: "))
    for i in range(round(x / 2)):
        if (i != 0):
            if (x % (i+1) == 0):
                return false
                break
            elif (i+1 == round(x/2)):
                return true
while not checkprime():
    checkprime()
def fibb(b2, b1):
    print(b1 + b2)
    fibb(b1, b1 + b2)
fibb(0,1)
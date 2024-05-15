T = int(input(""))

for i in range(T):
    (X, Y) = map (int, input("").split(" "))
    amount = min((X*3+Y*2), (Y*3+X*2), (X*3), (Y*2))
    print (amount)
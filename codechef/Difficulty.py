T = int(input())
for i in range(T):
    (X, Y) = map(int, input("").split(" "))
    if Y >=X and Y<=(X+200):
        print("YES")
    else:
        print("NO")
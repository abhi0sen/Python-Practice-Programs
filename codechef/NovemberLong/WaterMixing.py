T = int(input(""))

for i in range(T):
    (A, B, X, Y) = map(int, input("").split(" "))
    if A>B:
        if (A-B) <= Y:
            print("YES")
        else:
            print("NO")
    else:
        if (B-A) <= X:
            print("YES")
        else:
            print("NO")
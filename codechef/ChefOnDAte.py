T = int(input(""))
while T!=0:
    (x, y) = map(int, input().split(' '))
    
    if x>=y:
        print("YES")
    else:
        print("NO")

    T = T-1
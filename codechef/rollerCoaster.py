
T = int(input(""))
while T!=0:
    (x, h) = map(int, input().split(' '))
    
    if x>=h:
        print("YES")
    else:
        print("NO")

    T = T-1
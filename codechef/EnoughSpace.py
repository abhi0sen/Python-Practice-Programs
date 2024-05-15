# cook your dish here
T =int(input())

while(T!=0):
    (N, X, Y) = map(int, input().split(' '))
    save = X + Y*2

    if N>=save:
        print("YES")
    else:
        print("NO")
    
    T=T-1
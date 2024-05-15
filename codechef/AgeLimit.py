# cook your dish here
T =int(input())

while(T!=0):
    (X, Y, A) = map(int, input().split(' '))

    if A>=X and A<Y:
        print("YES")
    else:
        print("NO")
    
    T=T-1
# cook your dish here
T =int(input())

while(T!=0):
    (X, Y, Z) = map(int, input().split(' '))

    print(X*4+Y*2)
    
    T=T-1
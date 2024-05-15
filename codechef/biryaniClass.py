# cook your dish here
T =int(input())

while(T!=0):
    (X, Y) = map(int, input().split(' '))

    amount = X*Y  
    print(amount)
    
    T=T-1
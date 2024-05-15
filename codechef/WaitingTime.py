# cook your dish here
T =int(input())

while(T!=0):
    (K, X) = map(int, input().split(' '))
    Days = K*7

    remaining = Days - X 
    print(remaining)
    
    T=T-1
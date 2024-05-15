T =int(input())
i = 0
vol = 0

while(i<T):
    # X, Y = input().split()
    (X, Y) = map(int, input().split(' '))

    vol = max(X,Y) - min(X,Y)
    print(vol)
    
    i=i+1
T =int(input())
i = 0
vol = 0

while(i<T):
    # X, Y = input().split()
    (X, Y) = map(int, input().split(' '))

    
    if(X<Y):
        print("NO");
    else:
        print("YES");
    
    i=i+1
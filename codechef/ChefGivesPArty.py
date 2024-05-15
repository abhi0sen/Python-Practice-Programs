# cook your dish here

T = int(input(""))
while T!=0:
    (N, X, K) = map(int, input().split(' '))
    
    if (N*X <= K):
        print("YES")
    else:
        print("NO")

    T = T-1
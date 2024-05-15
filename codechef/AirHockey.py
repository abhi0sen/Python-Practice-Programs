
T = int(input(""))
while T!=0:
    (A, B) = map(int, input().split(' '))
    
    points = 7 - max(A, B)
    
    print(points)

    T = T-1
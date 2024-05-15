
T = int(input(""))
while T!=0:
    (A, B) = map(int, input().split(' '))
    if (A+B)%2 == 0:
        print("YES")
    else: 
        print("No")

    T = T-1
# cook your code here
# cook your code here
T = int(input(""))
while T!=0:
    (x, y) = map(int, input().split(' '))
    
    if x<y:
        print("B")
    elif y<x:
        print("A")

    T = T-1
# cook your code here
# cook your code here
T = int(input(""))
while T!=0:
    (X, Y) = map(int, input().split(' '))
    if X*2 < Y*5:
        print("Candy")
    elif X*2 > Y*5:
        print("Chocolate")
    else: 
        print("Either")

    T = T-1
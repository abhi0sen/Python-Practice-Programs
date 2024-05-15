# cook your code here
# cook your code here
T = int(input(""))
while T!=0:
    (a, b, c) = map(int, input().split(' '))
    
    # if a<b && b<c:
    
    value = max(a,b,c) - min(a,b,c)
    print (value)
    T = T-1
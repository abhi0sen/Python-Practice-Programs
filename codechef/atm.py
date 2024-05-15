def account(x, y):
    if (x>=2000 or x<0 or x>y):
        return y
    if (x%5!=0):
        return y
    z = (y-x)-0.50
    return z 

(a, b) = map(float, input().split(' '))

c = account(a, b)

print("{:.2f}".format(c))
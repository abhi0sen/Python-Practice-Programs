# A program to print the Fibonacci Series
nth = int(input("Enter the last term of fibonacci series: "))
n1 = 0
n2 = 1 
if (nth<=0):
    print("Your input is wrong!\n Kindly re-run the application and enter the value greater than 0")
elif (nth==n1):
    print(n1)
elif (nth==n2):
    print(n2)
else:
    li = [0, 1]
    for i in range(nth):
        nth = li[-1] + li[-2]
        li.append(nth)
    print(li) 
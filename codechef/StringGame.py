T = int(input(""))

for i in range(T):
    N = int(input())
    S = input("")
    
    Turn = 0
    
    A = ""
    B = ""
    t = 0
    
    while S != "":
        if Turn%2 == 0:
            if len(S)>t:
                A = A+S[t]
                S = S[0:t] + S[t+1:]
            else:
                A = A+S[t-1]
                S = S[0:t-1] + S[t:]
        else:
            if len(S)>t+1:
                B = B+S[t+1]
                S = S[0:t+1] + S[t+2:]
                t = t+1
            else:
                t = t-1
                if not t:
                    B = B+S[t]
                    S = S[0:t] + S[t+1:]
                else:
                    B = B+S[t-1]
                    S = S[0:t-1] + S[t:]
                
        Turn = Turn+1
    
    if A == B:
        print("YES")
    else:
        print("NO")
    print (A, B)
        
    
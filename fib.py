import json


def fb(N):
    
    N1, N2 = 0, 1    
    count = 0    
    num = []
    while count < N:
       nth = N1 + N2
       # update values
       N1 = N2
       N2 = nth
       count += 1
       num.append(N2)
    fib_set = {}
    fib_set["Member_count"] = len(num)
    fib_set["Sequence"] = num[0:]
    fib_set["Total-sum"] = sum(num)
    json_out = json.dumps(fib_set, indent=4)
    return json_out


    









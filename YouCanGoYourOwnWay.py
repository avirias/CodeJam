import random

def cal(n,lydia):
    l = int((n-1))
    g = ["E"*l+"S"*l,"S"*l+"E"*l]
    if(lydia in g):
        ans = [0]*(2*l)
        for i in range(l):
            while(1):
                no = random.randint(0,2*l-1)
                if(ans[no] == 0):
                    ans[no] = 'E'
                    break;
        ans = ['S' if x==0 else x for x in ans]
        path = ''.join(ans)
        return path
    else:
        return g[random.randint(0,1)]

def check(n,lydia):
    while(1):
        x = cal(n,lydia)
        if(x != lydia):
            return x

times = int(input())
size =[]
lydia = []
for i in range(times):
    size.append(int(input()))
    lydia.append(input())
    
for i in range(times):
    print("Case #"+str(i+1)+": "+check(size[i],lydia[i]))


def insort(inp,start=1):
    if start == len(inp):

        return inp
    ielm = inp[start]
    pos=findPos(ielm,inp[0:start],start)
    inp = move(inp,ielm,pos,start)

    return insort(inp,start+1)
def findPos(ielm,find,pos):
    if ielm < find[pos-1] and pos>0:
        return findPos(ielm,find,pos-1)
    else:
        return pos
def move(inp,ielm,pos,i):
    #print(i,pos)
    if i ==pos:
        inp[i] = ielm
        return inp
    inp[i] = inp[i-1]
    return move(inp,ielm,pos,i-1)

def allsub(l,temp:list,i=0):
    if i == len(l):
        all.append(temp.copy())
        return 
    allsub(l,temp,i+1)
    temp.append(l[i])
    allsub(l,temp,i+1)
    temp.pop()
def insortS(inp,start=1):
    for i in range(1,len(inp)):
        ielm = inp[i]
        for j in range(i,-1,-1):
            if len(ielm)<=len(inp[j-1]) and j>0:
                inp[j] = inp[j-1]
            else:
                inp[j]=ielm
                break
    for i in range(len(inp)-1,-1,-1):
        for j in range(len(inp)-1,-1,-1):
            if len(inp[i])==len(inp[j]):
                p =0
                while True:
                    if p< len(inp[i]):
                        if inp[i][p] < inp[j][p]:
                            inp[i],inp[j]=inp[i],inp[j]
                            break
                        elif inp[i][p] == inp[j][p]:
                            p+=1
                        else:
                            break
                    else:
                        break
    return inp



def printsum(inp:list,result):
    nosub = True
    for i in inp:
        if sum(i) == result:
            print(i)
            nosub = False
    if nosub:
        print("No Subset")
        
        
inp = [e for e in input("Enter Input : ").split("/")]
l = inp[1].split()
l=list(map(int, l))
res = int(inp[0])

l = insort(l)
all = []
temps=[]
allsub(l,[])
rset =[]
all = all[1:]
all = insortS(all)
#print(all)
printsum(all,res)


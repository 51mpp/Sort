
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


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "quick sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here
vess = []
for i in range(len(l)):
    vess.append(l[i])
    vess = insort(vess)
    print("list = {0} : ".format(l[:i+1]),end="")
    if len(vess)%2 ==0:
        #print((len(vess)/2)-1,(len(vess)/2))
        print("median =",(vess[int((len(vess)/2)-1)]+vess[int(len(vess)/2)])/2)
    else:
        print("median =",float(vess[int(len(vess)/2)]))
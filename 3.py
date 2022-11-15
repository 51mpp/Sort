def insort(inp,start=1):
    if start == len(inp):
        print()
        print("sorted")
        print(inp)
        return inp
    ielm = inp[start]
    pos=findPos(ielm,inp[0:start],start)
    inp = move(inp,ielm,pos,start)
    print("insert {0} at index {1} : {2} ".format(ielm,pos,inp[0:start+1]),end="")
    if inp[start+1:] != []:
        print(inp[start+1:])
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

inp = list(map(int,input("Enter Input : ").split(" ")))
insort(inp)
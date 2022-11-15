
        

def swapp(inp:list,i,swap,plus):
    if i+plus > len(inp)-1:
        return inp,i+plus,swap
    #print(inp,i)
    if inp[i+plus] <0:
        return swapp(inp,i,swap,plus+1)
    else:
        if inp[i]>inp[i+plus]:
            inp[i],inp[i+plus] = inp[i+plus],inp[i]
            return inp,i+plus,True
        return inp,i+plus,swap


inp = list(map(int,input("Enter Input : ").split(" ")))
for last in range(len(inp)-1,-1,-1):
    swap = False
    temp = inp[0]
    for i in range(last):
        inp,i,swap = swapp(inp,i,swap,1)
    if not swap:
        break

for i in inp:
    print(i,end=" ")
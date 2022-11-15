inp = list(map(int,input("Enter Input : ").split(" ")))
for last in range(len(inp)-1,-1,-1):
    swap = False
    temp = inp[0]
    for i in range(last):
        if inp[i]>inp[i+1]:
            inp[i],inp[i+1] = inp[i+1],inp[i]
            swap = True
            temp = inp[i+1]
            #print(inp)
    #print(temp)
    if not swap:
        print("last","step :",inp,'move[None]')
        break
    elif last ==1 and swap:
        print("last","step :",inp,'move[{0}]'.format(temp))
        break
    else:
        print(len(inp)-last,"step :",inp,'move[{0}]'.format(temp))
        
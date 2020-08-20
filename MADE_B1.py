
def cnt(data, ki):
#    dotx = []
#    doty = []
#    cx = 1
#    cy = 1
    out = 0
    #dotx.append([data[0][0]])
#    for i in range(ki):
#        for dx in dotx:
            #print(dx)
#            if(data[i][0] == dx):
#                cx+=1
#        if cx == 1:
#            dotx.append([data[i][0]])
        #cc.append(c)
    #doty.append([data[0][1]])
#    for i in range(ki):
#        for dy in doty:
            #print(dy)
#            if (data[i][1] == dy):
#                 cy += 1
#        if cy == 1:
#            doty.append([data[i][1]])
        #cc.append(c)
#    for i in range(len(dotx)):
#        for j in range(i + 1, len(dotx)):
#            if(dotx[i] == dotx[j]):
#                for m in range(i + 1, len(doty)):
#                    if (doty[i] == doty[m] or doty[j] == doty[m]):
#                        for n in range(m + 1, len(doty)):
#                            if(dotx[m] == dotx[n] and (doty[m] == doty[i] and (doty[n] == doty[j]) or (doty[m] == doty[j] and doty[n] == doty[i]))):
#                                out += 1
                                #print(i, j, m, n)

    ci = []
    cj = []


    ciy = []
    cjy = []

    for i in range(0, ki):
        for j in range(i + 1, ki):
            if (data[i][0] == data[j][0]):
                #dx1 = data[i][0]
                #dx2 = data[j][0]
                #if((ci!=i and cj!=j) or (ci == 0 and cj == 0)):
                #    if ((data[ci][1] == data[i][1] and data[cj][1] == data[j][1])):
                #        out+=1
                #        print(ci, cj, i, j)
                ci.append(i)
                cj.append(j)
            #if(data[i][1] == data[j][1]):
            #    ciy.append(i)
            #    cjy.append(j)
    #print(ci, cj)
    #print(ciy, cjy)

#print(ci, cj)
            #if ((data[ci][1] == data[i][1] and data[cj][1] == data[j][1]) and (ci!=i or cj!=j)):
            #    out += 1
            #    ci.append(i)
            #    cj.append(j)
    for i in range(0, len(ci)):
        for j in range(i+1, len(cj)):
            if ((data[ci[i]][1] == data[ci[j]][1] and data[cj[i]][1] == data[cj[j]][1]) or (data[ci[i]][1] == data[cj[j]][1] and data[cj[i]][1] == data[ci[j]][1])):
            #if(data[ci[i]][1] == data[ciy[j]][1] )
                out+=1
                #print(i, j)
    return out

x = int(input())
k = []
data = []
res = []
for i in range(x):
    k.append(int(input()))
    buflist = []
    for j in range(k[i]):
        buflist.append(list(map(int, input().rstrip().split())))
        #data.append([list(map(int, input().rstrip().split()))])
    data.append(buflist)
for i in range(x):
    #res.append(cnt(data[i], k[i]))
    print(cnt(data[i], k[i]))
#for i in range(x):
#    print(res[i])
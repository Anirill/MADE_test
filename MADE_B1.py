
def cnt(data, ki):
    out = 0
    ci = []
    cj = []
    for i in range(0, ki):
        for j in range(i + 1, ki):
            if (data[i][0] == data[j][0]):
                ci.append(i)
                cj.append(j)
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
import numpy as np





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
    #print(cnt(data[i], k[i]))
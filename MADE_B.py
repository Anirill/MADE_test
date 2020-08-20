


def trckcnt(crrds, ki):
    ans = 0
    c1 = c2 = c3 = c4 = crrds[0]
    for i in range(ki):
        for j in range(i+1, ki):
            if (crrds[i][0] == crrds[j][0]):
                for ii in range(j+1, ki):
                    if (crrds[i][1] == crrds[ii][1]):
                        for jj in range(ii + 1, ki):
                            if ((crrds[j][1] == crrds[jj][1]) and (crrds[ii][0] == crrds[jj][0])):
                                ans += 1
                                ii += 1
                                jj = ii + 1
                    else:
                        if (crrds[j][1] == crrds[ii][1]):
                            for jj in range(ii + 1, ki):
                                if ((crrds[i][1] == crrds[jj][1]) and (crrds[ii][0] == crrds[jj][0])):
                                    ans += 1
                                    ii += 1
                                    jj = ii + 1

            else:
                if (crrds[i][1] == crrds[j][1]):
                    for ii in range(j + 1, ki):
                        if (crrds[i][0] == crrds[ii][0]):
                            for jj in range(ii + 1, ki):
                                if ((crrds[j][0] == crrds[jj][0]) and (crrds[ii][1] == crrds[jj][1])):
                                    ans += 1
                                    ii += 1
                                    jj = ii + 1
                        else:
                            if (crrds[j][0] == crrds[ii][0]):
                                for jj in range(ii + 1, ki):
                                    if ((crrds[i][0] == crrds[jj][0]) and (crrds[ii][1] == crrds[jj][1])):
                                        ans += 1
                                        ii += 1
                                        jj = ii + 1
    return ans

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
    print(trckcnt(data[i], k[i]))

#for i in range(x):
#    print(res[i])
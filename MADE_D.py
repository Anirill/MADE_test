
#def isclose(tag1, tag2):
#    if(tag1 == (tag2[0]+'/'+tag2[1:])):
#        #print(tag2[0]+'/'+tag2[1:])
#        return True
#    return False
def iscorrect(data, ki):
    buf = []
    c = 0
    buf.append(data[0])
    for j in range(1, ki):
        if (c >= 0):
            if ((data[j] == (buf[c][0]+'/'+buf[c][1:])) or buf[c] == ''):
                c -= 1
            else:
                c += 1
                if (c < len(buf)):
                    buf.insert(c, data[j])
                else:
                    buf.append(data[j])
        else:
            c += 1
            buf[0] = data[j]
    return buf, c

x = int(input())
k = []
data = []
res = []
buf1 = []
c1 = 0
buf2 = []
c2 = 0
out = ''

for i in range(x):
    k.append(int(input()))
    buflist = []

    for j in range(k[i]):
        buflist.append(input().upper().rstrip())
        #data.append([list(map(int, input().rstrip().split()))])
    data.append(buflist)
for i in range(x):
    if (k[i] == 0):
        print('CORRECT')
    else:
        out = ''
        buf1, c1 = iscorrect(data[i], k[i])
        if (c1 == -1):
            print('CORRECT')
        else:
            out = buf1[c1 // 2]
            del buf1[c1 // 2]
            buf2, c2 = iscorrect(buf1, c1 - 1)
            if (c2 <= 0):
                print('ALMOST', out)
            else:
                print('INCORRECT')
#for i in range(x):
#    #res.append(cnt(data[i], k[i]))
#    print(data[i])
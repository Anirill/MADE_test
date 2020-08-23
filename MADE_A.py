def generate(ki):
    a = 0b01
    b = 0b01
    div = 1
    div1 = 1
    ans = 0
#    if (ki == 1):
#        return (a + b)
    i = 0
    while(ki >= div):
        i += 1
        a = a << 1
        div += (i)
    b = b << (ki - div + i)
    ans = a + b
    return ans

x = int(input())
k = []
res = []

for i in range(x):
    k.append(int(input()))
for i in range(x):
    res.append((generate(k[i])) % 35184372089371)
for i in range(x):
    print(res[i])
def math_tree(basetree, ki):
    sum = 0
    tree = []
    tree.append([1 << (ki - 1)])
    for i in range(1, ki):
        row = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(int((tree[i - 1][0] // 2)))
            else:
                row.append(int((tree[i - 1][j - 1] + tree[i - 1][j]) // 2))
        tree.append(row)
    for i in range(0, ki):
        for j in range(0, (i+1)):
            sum += (basetree[i][j] * tree[i][j])
    return sum
x = int(input())
k = []
data = []
tree = []
res = []
row = []
m = []
buf_n = 0
h = 63

for i in range(x):
    k.append(int(input()))
    buflist = []
    for j in range(k[i]):
        buflist.append(list(map(int, input().rstrip().split())))
    data.append(buflist)
for i in range(x):
    buf_n = math_tree(data[i], k[i])
    buf_m = 1 << (k[i] - 1)
    while ((buf_n % 2) == 0 and (buf_m % 2) == 0):
        buf_n = int(buf_n // 2)
        buf_m = int(buf_m // 2)
    res.append(buf_n)
    m.append(buf_m)
for i in range(x):
    print(res[i], m[i], sep = ' ')

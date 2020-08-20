
def max_subarray(numbers, k, max_len):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if (current_sum <= 0) and (current_end != k) and ((current_end != k + max_len) or k < 0):
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        elif (current_end == k or current_end == k + max_len) and k >= 0:
            current_sum = 0
            current_start = current_end + 1
        else:
            # Extend the existing sequence with the current element
            current_sum += x
        if current_sum > best_sum and ((current_end - current_start) < (max_len)):
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive
            if (best_end - best_start) >= (max_len):
                return best_sum #, best_start, best_end

    return best_sum #, best_start, best_end


res = []
arrm = []
arrm2 = []
arrmlen = []
km = []
nbtests = int(input())
for i in range(nbtests):
    arrlen, k = list(map(int, input().rstrip().split()))
    arrmlen.insert(i, arrlen)
    km.insert(i, k)
    arr = list(map(int, input().rstrip().split()))
    arrm.insert(i, arr + arr)
    arr.reverse()
    arrm2.insert(i, arr + arr)
for i in range(nbtests):
    a = max_subarray(arrm[i], km[i], arrmlen[i])
    km2 = -1;
    if (km[i] != -1):
        km2 = arrmlen[i] - km[i] - 1
    b = max_subarray(arrm2[i], km2, arrmlen[i])
    if a >= b:
        res.insert(i, a)
    else:
        res.insert(i, b)
#for i in range(nbtests):
#    if ()
#    res.insert(i, max_subarray(arrm[i], km[i], arrmlen[i]))
for i in range(nbtests):
    print(res[i])

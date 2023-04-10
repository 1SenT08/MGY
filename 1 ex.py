import sys


def helps(num, lst, n):
    flag = True
    c = num
    try:
        while flag:
            if abs(lst[c] - lst[c] + 1) <= n:
                c += 1
            else:
                return c
    except:
        return c


n = int(input())
right_words = input()
strk2 = []
for i in sys.stdin:
    strk2.append(i.rstrip())

a = []
for i in right_words:
    a.append(i)

bst = []
for strk in strk2:
    the_best_res = []
    for i in range(len(strk)):
        if strk[i] in a:
            the_best_res.append(i)

    best = []
    for i in range(len(the_best_res)):
        v = []
        v.append(i)
        try:
            while abs(the_best_res[i] - the_best_res[i + 1]) <= n:
                i += 1
            v.append(i)
            best.append(v)

        except:
            v.append(i)
            best.append(v)

    d = [0, 0]
    for i in best:
        if i[1] - i[0] > d[1] - d[0]:
            d = i
    try:
        bst.append(strk[the_best_res[d[0]]:the_best_res[d[1]] + 1])
    except:
        bst.append('0')

mx = ''
for i in bst:
    if len(mx) < len(i):
        mx = i

print(mx)
import helper as hp

a = hp.create()

b = hp.create()

n = len(a)
m = len(a[0])

for k in range(n):
    for i in range(k+1, n):
        factor = a[i][k] / a[k][k]
        for j in range(k, m):
            a[i][j] -= factor * a[k][j]
        b[i][0] -= factor * b[k][0]

x = [0]*n
for i in range(n-1, -1, -1):
    sum_ax = 0
    for j in range(i+1, n):
        sum_ax += a[i][j] * x[j]
    x[i] = (b[i][0] - sum_ax) / a[i][i]

print('Result: ', x)

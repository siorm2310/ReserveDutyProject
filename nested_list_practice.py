a = [0 for i in range(30)]
b = [i+1 for i in range(28)]

#1
n = 0
for i in range(30):
    if not (i == 14 or i == 18):
        a[i] = b[n]
        n += 1

#2
c = [[a[i] for i in range(30)] for j in range(33)]

#3
v = [[2*i+1, 2*i+2] for i in range(33)]
for i in range(33):
    c[i][14] = v[i][0]
    c[i][18] = v[i][1]


for row in c:
    print (row)
x = int(input())
y = int(input())
n = int(input())
#print ([x*x for x in range(1,6)])
print([[i, j] for i in range(x + 1) for j in range(y + 1) if ((i + j) != n)])

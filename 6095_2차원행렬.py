matrix = []
col = 0

for row in range(3):
    matrix.append([])
    for col in range(3):
        matrix[row].append(0)

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    matrix[x-1][y-1] = 1

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

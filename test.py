#  1. 개미굴 변수 생성 및 입력값 받기  
matrix = []
for row in range(10):
    matrix.append(list(map(int,input().split())))

#  2. 개미 이동 경로 
# 간과한점 - ant로 행렬의 값 가진 변수 만들어도 실제값에서 변경해야함 
#            ant=9로 한다고 실제 행렬값 바뀌는게 아님
x=1
y=1
while True:
    if matrix[x][y]==0:
        matrix[x][y]=9
    elif matrix[x][y]==2:
        matrix[x][y]=9
        break

    if matrix[x][y+1]!=1:
        y+=1
    elif matrix[x+1][y]!=1:
        x+=1
    
    if (matrix[x][y+1]==1 and matrix[x+1][y]==1):
        break

#  3. 경로 출력
for i in range(10):
    for j in range(10):
        print(matrix[i][j],end='')
    print()
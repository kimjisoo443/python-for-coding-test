# 1. 내 코드
n,m = map(int,input().split())
small_list = []
for i in range(n):
    list_n = list(map(int,input().split()))
    list_n.sort()
    small = list_n[0]
    small_list.append(small)

small_list.sort()
print(small_list[-1])

# 2.책 - min이용
result = 0
for i in range(n):
    list_n2 = list(map(int,input().split()))
    min_val = min(list_n2)
    result = max(result, min_val)
    # print(f"result : {result}")
print(f"2번 답안 : {result}")

# 3. 책 - 이중반복문
result = 0
for i in range(n):
    list_n3 = list(map(int,input().split()))
    min_value = 1001

    for j in list_n3:
        min_value = min(min_value,j)

    result = max(result,min_value)

print(f"3번 답안 : {result}")

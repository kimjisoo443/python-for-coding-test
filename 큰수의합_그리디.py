n,m,k = map(int,input().split())
list_n = list(map(int,input().split()))
list_n.sort()
first=list_n[-1]
second=list_n[-2]

sum=0
count=0
while count!=m:
    for j in range(k):
        count+=1
        sum+=first
        # print(f"{count} : {sum}")
    count+=1
    sum+=second
    # print(f"{count} : {sum}")
print(sum)

print(m//(k+1)*(k*first+second) + m%(k+1)*k)
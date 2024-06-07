n,m,k = map(int,input().split())
list_n = list(map(int,input().split()))
list_n.sort()
first=list_n[-1]
second=list_n[-2]
#1
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

#2.식으로 풀기
print(m//(k+1)*(k*first+second) + m%(k+1)*k)

#3. 책
c = (m/(k+1))*k
c+=m%(k+1)
result = 0
result += c*first
result += (m-c)*second
print(result)

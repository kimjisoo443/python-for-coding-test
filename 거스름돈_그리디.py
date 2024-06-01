money = int(input())
a=money//500
b=(money%500)//100
c=((money%500)%100)//50
d=(((money%500)%100)%50)//10
print(a+b+c+d)

count=0
list = [500,100,50,10]
for i in list:
    count += money//i
    money=money%i
print(count)
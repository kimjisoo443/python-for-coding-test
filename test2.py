# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 123+321=444
# 2 9 10 21 24 => 2.0 9.0 두자리면 /10 => 1.0 2.1 2.4
# 9 24 2 21 10
# 세자리면 333 444 555 /100 비교
import sys 

list = input().split()
list.sort(reverse=True) #내림차순 정렬
print(list)
# for entry in enumerate(list):
#     if(any(100>num for num in list)):

if any(100<num for num in list):
    print("세자리수가 포함되지 않는 리스트 입력")
    if (len(list)>6):
        sys.exit("-1")
elif any(100>num for num in list):
    if(len(list)>9):
        sys.exit("-1")
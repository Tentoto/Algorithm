'''
문제 이름 : 홀짝
문제 내용 : 주어진 n번째 홀짝 수열의 원소를 출력하는 문제.
'''
from decimal import *
n=int(input())
getcontext().prec=101
print(2*n-int((Decimal(8*n-7).sqrt()+1)/2))
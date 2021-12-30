'''
문제 이름 : A+B - 5
문제 내용 : 두 정수 입력의 합을 출력하는 문제
'''
import sys
inputs = sys.stdin.readlines()
for line in inputs:
    a, b = map(int, line.split())
    if a+b:
        print(a+b)
    else:
        break
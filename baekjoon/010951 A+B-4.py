'''
URL : https://www.acmicpc.net/problem/10951
문제 이름 : A+B-4
문제 내용 : 두 정수 입력의 합을 출력하는 문제
'''
import sys
inputs = sys.stdin.readlines()
for line in inputs:
    a, b = map(int, line.split())
    print(a+b)
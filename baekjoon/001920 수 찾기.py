'''
URL : https://www.acmicpc.net/problem/1920
문제 이름 : 수 찾기
문제 내용 : 주어진 수열 안에 다시금 주어진 수열의 원소들의 존재여부를 출력하는 문제
'''
input()
nums=set(input().split())
input()
for i in input().split():
    print(1 if i in nums else 0)
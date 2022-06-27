'''
URL : https://www.acmicpc.net/problem/9996
문제 이름 : 한국이 그리울 땐 서버에 접속하지
문제 내용 : 두 알파벳 사이에 *이 있는 문자열이 주어졌을 때 다음으로 입력되는 문자열들이 앞 알파벳으로 시작하고 뒤의 알파벳으로 끝나는 문자열인지 판단하는 문제
'''
import re
repeat=int(input())
word=input().split('*')
pattern=re.compile(f'^{word[0]}(.*){word[1]}$')
for _ in range(repeat):
    if re.match(pattern, input()):
        print('DA')
    else:
        print('NE')
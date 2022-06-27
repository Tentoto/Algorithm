'''
URL : https://www.acmicpc.net/problem/10491
문제 이름 : Quite a problem
문제 내용 : 주어지는 여러 줄의 입력에 problem이 들어있으면 yes 없으면 no를 출력.
'''
import sys
import re
pat=re.compile('problem')
sentences=sys.stdin
for sentence in sentences:
    print('yes' if re.search(pat,sentence.lower()) else 'no')

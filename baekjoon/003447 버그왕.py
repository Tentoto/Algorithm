'''
URL : https://www.acmicpc.net/problem/3447
문제 이름 : 버그왕
문제 내용 : 주어진 여러 줄의 문자열에서 BUG를 제거한 결과를 출력
'''
import sys
import re
pat=re.compile('BUG')
sentences=sys.stdin.readlines()
for sentence in sentences:
    while sentence!=re.sub('BUG','',sentence):
        sentence=re.sub('BUG','',sentence)
    print(sentence,end='')
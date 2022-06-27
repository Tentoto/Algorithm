'''
URL : https://www.acmicpc.net/problem/17413
문제 이름 : 단어뒤집기 2
문제 내용 : <tag>는 그대로 두고 나머지 소문자 알파벳과 숫자로 이루어진 단어들이 공백으로 구분된 문자열을 
단어별로 뒤집어서 출력하는 문제
'''
import re

extract=re.findall('(<[a-z ]+>)|([a-z0-9 ]+)',input())
answer=''.join([i[0] if i[0] else ' '.join(map(lambda x: x[::-1],i[1].split())) for i in extract])

print(answer)
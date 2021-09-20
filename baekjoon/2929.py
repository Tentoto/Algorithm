'''
문제 이름 : 머신코드
문제 내용 : 알파벳 대문자와 소문자로 이루어진 문자열 입력에서 대문자를 4의 배수에 해당하는 곳에 위치시키기 위해 필요한 추가적인 문자 수를 출력하는 문제

'''
import re
pat=re.compile('[A-Z]')
answer=0
for match in re.finditer(pat,input()):
    if (match.span()[0]+answer)%4!=0:
        answer+=4-(match.span()[0]+answer)%4
print(answer)
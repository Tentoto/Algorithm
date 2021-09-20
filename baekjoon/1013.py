'''
문제 이름 : Contact
문제 내용 : 다음의 규칙을 따르면 YES 아니면 NO을 출력하는 문제.
    (100+1+ | 01)+

'''
import re
for _ in range(int(input())):
    print('YES' if re.match('^(100+1+|01)+$',input()) else 'NO')
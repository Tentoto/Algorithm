'''
문제 이름 : 잠수함식별
문제 내용 : 다음의 규칙을 따르면 SUBMARINE 아니면 NOISE을 출력하는 문제.
    (100+1+ | 01)+

'''
import re
print('SUBMARINE' if re.match('^(100+1+|01)+$',input()) else 'NOISE')
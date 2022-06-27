'''
URL : https://www.acmicpc.net/problem/9012
문제 이름 : 괄호
문제 내용 : 괄호가 올바르면 YES 아니면 NO를 출력하는 문제
'''
import re
for _ in range(int(input())):
    text=input()
    while text:
        text=re.sub('\(\)','',text)
        if re.fullmatch('\(+|\)+|\)+\(+',text):
            break
    print('NO' if text else 'YES')

'''    
for _ in range(int(input())):
    stack=[]
    for p in input():
        if not stack and p==')':
            stack.append(p)
            break
        elif p==')':
            stack.pop()
        else:
            stack.append(p)
    if stack:
        print('NO')
    else:
        print('YES')'''
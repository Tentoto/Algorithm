'''
URL : https://www.acmicpc.net/problem/1074
문제 이름 : Z
문제 내용 :
'''
N, r, c = map(int, input().split())
step=''
answer=0
for M in range(N-1,-1,-1):
    if r<2**M:
        if c<2**M:
            step+='0'
        else:
            step+='1'
    else:
        if c<2**M:
            step+='2'
        else:
            step+='3'
    r-=2**M*(r>=2**M)
    c-=2**M*(c>=2**M)

for i,s in enumerate(step[::-1]):
    answer+=int(s)*4**i
print(answer)
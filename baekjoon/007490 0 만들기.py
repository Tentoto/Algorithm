'''
URL : https://www.acmicpc.net/problem/7490
문제 이름 : 0 만들기
문제 내용 : 주어진 n에 대해 1부터 n까지의 수를 더하고 빼고 이어붙이는 연산을 통해 0을 만들 수 있는 경우들을 전부 출력
'''
def comb_operators(n):
    operator={0:' ',1:'+',2:'-'}
    comb_op=[]
    for i in range(3**n):
        op=''
        while i>0:
            op=operator[i%3]+op
            i//=3
        comb_op.append(' '*(n+1-len(op))+op)
    return comb_op

for _ in range(int(input())):
    n=int(input())
    for comb in comb_operators(n-1):
        equation=''
        ev_eq=''
        for op,num in zip(comb,list(map(str,range(1,n+1)))):
            equation+=op+num
            ev_eq+=op*(op!=' ')+num
        if eval(ev_eq)==0:
            print(equation.strip())
    print()
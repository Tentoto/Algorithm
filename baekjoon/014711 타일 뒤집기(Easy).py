'''
URL : https://www.acmicpc.net/problem/14711
문제 이름 : 타일 뒤집기(Easy)
문제 내용 : 첫 줄의 흑백 타일이 주어졌을 때 흑타일이었던 자리를 다 뒤집었을 때 전체를 백타일로 만드는 게임판 만들기.
           타일을 뒤집을 때는 인접한 타일도 뒤집어진다.
'''
def flip(line,affected_line):
    flipped=[0 for _ in range(len(line))]
    for idx,color in enumerate(line):
        if color=='#':
            flipped[idx]+=1
            if idx>0:
                flipped[idx-1]+=1
            if idx<len(line)-1:
                flipped[idx+1]+=1
    next_line=[cell if flipped[idx]%2==0 else ['#','.'][cell=='#'] for idx,cell in enumerate(affected_line)]
    affected_line=[cell if line[idx]=='.' else ['#','.'][cell=='#'] for idx,cell in enumerate(next_line)]
    return ''.join(next_line),''.join(affected_line)

n=int(input())
line=input()
affected_line=line[:]
for _ in range(n):
    print(line)
    line,affected_line=flip(line,affected_line)
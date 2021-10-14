'''
문제 이름 : 박스 그림 문자
문제 내용 : 주어진 박스 그림 문자에서 빈 공간을 이웃한 문자들에 맞게 채워서 출력하는 문제
'''
beautiful=[]
n,m=map(int,input().split())
for _ in range(n*3):
    beautiful.append([i for i in input()])
for r in range(n):
    for c in range(m):
        i=3*r+1
        j=3*c+1
        if (i+j)%2==0:
            continue
        beautiful[i][j]='#'
        try:
            if beautiful[i-2][j]=='#':
                beautiful[i-1][j]='#'
        except:
            pass
        try:
            if beautiful[i+2][j]=='#':
                beautiful[i+1][j]='#'
        except:
            pass
        try:
            if beautiful[i][j-2]=='#':
                beautiful[i][j-1]='#'
        except:
            pass
        try:
            if beautiful[i][j+2]=='#':
                beautiful[i][j+1]='#'
        except:
            pass
for line in beautiful:
    print(*line,sep='')
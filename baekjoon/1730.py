'''
문제 이름 : 판화
문제 내용 : 주어진 크기의 정사각형 배열에 주어진 지시에 따라 움직였을 때 지나간 방향에 따라 경로 상에 적절한 문자를 담아 출력하는 문제.
'''
n=int(input())
blueprint=[[[0,0] for _ in range(n)] for _ in range(n)]
x_pos=0
y_pos=0
for instruction in input():
    disp_y=(-1)**(instruction=='U')*(instruction in ['D','U'])
    disp_x=(-1)**(instruction=='L')*(instruction in ['L','R'])

    if disp_y and y_pos+disp_y in range(n):
            blueprint[y_pos][x_pos][0]=disp_y
            y_pos=y_pos+blueprint[y_pos][x_pos][0]
            blueprint[y_pos][x_pos][0]=disp_y

    if disp_x and x_pos+disp_x in range(n):
            blueprint[y_pos][x_pos][1]=disp_x
            x_pos=x_pos+blueprint[y_pos][x_pos][1]
            blueprint[y_pos][x_pos][1]=disp_x

for line in blueprint:
    prints=''
    for inst in line:
        if inst[0]*inst[1]:
            prints+=chr(43)
        elif inst[0]:
            prints+=chr(124)
        elif inst[1]:
            prints+=chr(45)
        else:
            prints+=chr(46)
    print(prints)
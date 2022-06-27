'''
URL : https://www.acmicpc.net/problem/2818
문제 이름 : 숙제하기 싫을 때
문제 내용 : 주사위를 주어진 row와 column에 따라 'ㄹ'자로 굴려서 나오는 주사위 숫자를 다 더한 값을 출력하는 문제
'''
dice={1:[3,2,4,5],
      2:[1,3,6,4],
      3:[2,1,5,6],
      4:[1,2,6,5],
      5:[3,1,4,6],
      6:[2,3,5,4]}
row,col=map(int,input().split())
axis=2
top=1
idx=0
direction=-1
lap=col//4
remain=col%4
answer=14*lap*row

for r in range(row):
    top=7-axis
    roll=[dice[axis][(idx+i*direction)%4] for i in range(remain)]
    answer+=sum(roll)
    axis=dice[axis][(idx+(remain-1)*direction)%4]
    idx=dice[axis].index(top)
    direction*=-1
print(answer)
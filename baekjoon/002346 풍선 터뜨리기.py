'''
URL : https://www.acmicpc.net/problem/2346
문제 이름 : 풍선 터뜨리기
문제 내용 : 풍선의 수가 주어지고 풍선 안의 종이에 적힌 숫자에 대한 정보가 주어진다. 
           첫번째 풍선부터 터뜨려 풍선 안의 종이에 적힌 숫자만큼 이동하여 터뜨릴 때 터진 풍선의 번호를 순서대로 출력
'''
answer=[]
n=int(input())
balloons=[(idx+1,memo) for idx,memo in enumerate(map(int,input().split()))]
pos=0

while balloons:
    pos=(len(balloons)+pos)%len(balloons)
    balloon=balloons.pop(pos)
    answer.append(balloon[0])
    memo=balloon[1]
    pos+=memo-(memo>0)

print(*answer)
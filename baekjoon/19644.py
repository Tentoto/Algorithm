'''
문제 이름 : 좀비 떼가 기관총 진지에도 오다니
문제 내용 : 주어진 기관총 세부 능력치와 좀비떼의 체력이 주어졌을 때 살아남는지 여부
'''
import sys
input=sys.stdin.readline

street=int(input())
ef_range, damage=map(int,input().split())
num_of_grenade=int(input())
zombies=[]
used_grenade=0

for i in range(street):
    if i>=ef_range:
        used_grenade-=zombies[i-ef_range]
    zombie=int(input())
    if zombie>(min(ef_range,(i+1))-used_grenade)*damage:
        num_of_grenade-=1
        if num_of_grenade<0:
            print('NO')
            break
        zombies.append(1)
        used_grenade+=1
    zombies.append(0)
else:
    print('YES')
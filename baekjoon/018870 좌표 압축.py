'''
URL : https://www.acmicpc.net/problem/18870
문제 이름 : 좌표 압축
문제 내용 :
'''
input()
ind={}
coordinates=list(map(int,input().split()))
for i,coord in enumerate(sorted(set(coordinates))):
    ind[coord]=i

print(*[ind[coord] for coord in coordinates])
'''
문제 이름 : 평행 우주
문제 내용 : 주어진 행성 간 거리의 양의 정수배일 때 이동이 가능하다. 
            출발 이후 감속만 가능할 때 초기 속도는 얼마여야 하는가?
'''
input()
planets=list(map(int,input().split()))[::-1]
answer=0
for dist in planets:
    if answer<=dist:
        answer=dist
    else:
        answer=int(((answer-.1)//dist+1)*dist)
print(answer)


'''
문제 이름 : 과제
문제 내용 : 제출 기한, 과제 점수 쌍을 입력받아 가장 높은 점수를 내는 문제
'''
from collections import defaultdict
dic=defaultdict(list)
for _ in range(int(input())):
    n,m=map(int,input().split())
    dic[n].append(m)

decides=[0 for _ in range(max(dic))]

for i in sorted(dic.keys()):
    assignments=sorted(dic[i])
    decides[i-1]=assignments[-1]
    for a in assignments[:-1]:
        try:
            if min(decides[:i-1])<a:
                decides[decides.index(min(decides[:i-1]))]=a 
        except:
            pass
            
print(sum(decides))




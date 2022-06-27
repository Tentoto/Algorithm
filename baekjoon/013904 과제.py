'''
URL : https://www.acmicpc.net/problem/13904
문제 이름 : 과제
문제 내용 : 제출 기한, 과제 점수 쌍을 입력받아 가장 높은 점수를 내는 문제
'''
from collections import defaultdict
dic=defaultdict(list) #입력을 저장할 dictionary
for _ in range(int(input())): #첫 입력은 과제의 수
    n,m=map(int,input().split()) #공백으로 구분된 과제 제출 기한과 점수 쌍을 입력 받아 dictionary에 저장
    dic[n].append(m)

decides=[0 for _ in range(max(dic))] #어떤 과제를 풀기로 선택했는지 결과를 저장하는 list

for i in sorted(dic.keys()): #제출 기한을 오름차순에 따라 추출
    assignments=sorted(dic[i]) #추출된 제출 기한에 해당하는 과제들 점수를 오름차순으로 정렬
    decides[i-1]=assignments[-1] #제출 기한 당일에는 최고점의 과제를 수행
    for a in assignments[:-1]: #나머지 과제들의 점수가 이전 제출 기한의 과제들보다 높으면 최소 점수의 과제부터 교체
        try:
            if min(decides[:i-1])<a:
                decides[decides.index(min(decides[:i-1]))]=a 
        except:
            pass
            
print(sum(decides))





'''
문제 이름 : 나는 위대한 슈퍼스타K
문제 내용 : n명의 참가자들의 m개의 장르에 대한 점수를 내림차순으로 입력받아 k명을 합격시켰을 때 최대 점수를 만드는 문제. 동일 장르 다수 합격 허용.
'''
def solution():
	dic={}
	n,m,k=map(int,input().split()) #공백으로 구분된 참가자 수, 장르 수, 합격자 수를 입력받는다.
	for i in range(1,n+1): #dictionary 초기화. defaultdict를 사용했으면 되는데..
		dic[str(i)]=0
	for _ in range(m): #m개의 장르에 대한 공백으로 구분된 전체 참가자 번호와 점수를 입력받는다.
		scores=input().split() #입력받은 list로 짝수 index는 참가자 번호, 홀수 index는 점수이다.
		for i in range(n):
			dic[scores[2*i]]=max(dic[scores[2*i]],float(scores[2*i+1])) #한 사람은 한 장르만 부를 수 있기에 dictionary의 값과 비교하여 큰 값을 저장

	print(round(sum(sorted(dic.values(),reverse=True)[:k]),1)) #점수가 높은 순으로 정렬하여 k명을 뽑아 점수의 합을 출력
    
solution()

'''
문제 이름 : 나는 위대한 슈퍼스타K
문제 내용 : n명의 참가자들의 m개의 장르에 대한 점수를 내림차순으로 입력받아 k명을 합격시켰을 때 최대 점수를 만드는 문제. 동일 장르 다수 합격 허용.
'''
def solution():
	dic={}
	n,m,k=map(int,input().split())
	for i in range(1,n+1):
		dic[str(i)]=0
	for _ in range(m):
		scores=input().split()
		for i in range(n):
			dic[scores[2*i]]=max(dic[scores[2*i]],float(scores[2*i+1]))

	print(round(sum(sorted(dic.values(),reverse=True)[:k]),1))
    
solution()
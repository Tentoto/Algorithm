'''
URL : https://www.acmicpc.net/problem/19818
문제 이름 : LaTeX Expert
문제 내용 : Bibliography를 정렬 여부를 반환하고 정렬이 틀린 경우 제대로 정렬된 형태를 반환.
'''
import sys
import re

lines=fr"{''.join(sys.stdin.readlines())}"
split_point=re.search(r'\\begin',lines).span()[0]
p=lines[split_point:]
bib=list(filter(None,p.split('\n')))

order=[name.group(1) for name in re.finditer(re.compile('cite\{([a-z]{1,100})\}'),lines)]
bib_order=[name.group(1) for name in re.finditer(re.compile('bitem\{([a-z]{1,100})\}'),lines)]

if order==bib_order:
    print('Correct')
else:
    print('Incorrect')
    print(bib[0])
    print(*sorted(bib[1:-1],key=lambda x:order.index(re.search(re.compile('ibitem\{([a-z]{1,100})\}'),x).group(1))),sep='\n')
    print(bib[-1])




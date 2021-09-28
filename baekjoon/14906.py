'''
문제 이름 : 스러피
문제 내용 : 스러피의 존재여부 판단
'''
import re

slump='((D|E)F+)+G'
slimp='AH'
slimp3=f'A{slump}C'
slimp2=f'(AB)+({slimp}|{slimp3})C+'

repeat=int(input())
print('SLURPYS OUTPUT')
for _ in range(repeat):
    text=input()
    if re.match(slimp+slump,text):
        if re.match(slimp+slump,text).group()==text:
            print('YES')
        else:
            print('NO')
    elif re.match(slimp2+slump,text):
        if text.count('A')==text.count('C')+text.count('H') and re.match(slimp2+slump,text).group()==text:
            print('YES')
        else:
            print('NO')
    elif re.match(slimp3+slump,text):
        if re.match(slimp3+slump,text).group()==text:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
print('END OF OUTPUT')
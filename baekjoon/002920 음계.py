'''
URL : https://www.acmicpc.net/problem/2920
문제 이름 : 음계
문제 내용 : 
'''
ascend=True
descend=True
prev_note=None

for note in map(int,input().split()):
    if not prev_note:
        prev_note=note
    else:
        if note>prev_note:
            descend=False
        elif note<prev_note:
            ascend=False
        prev_note=note

print('ascending' if ascend else 'descending' if descend else 'mixed')
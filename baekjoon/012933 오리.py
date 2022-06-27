"""
URL : https://www.acmicpc.net/problem/12933
제목 : 오리
내용 : 오리의 울음 소리는 quack이다. 여러 마리의 울음 소리는 섞일 수 있지만, 순서가 바뀔 순 없다. 울음 소리가 주어졌을 때 오리가 몇 마리 있는지 출력하고 잘못된 울음 소리라면 -1을 출력한다.
입력 : 'q','u','a','c','k'로만 이루어진 소리가 주어진다. 소리의 길이는 5보다 크거나 같고 2500보다 작거나 같다.
출력 : 오리의 최소 수를 출력하고 올바르지 않은 소리라면 -1을 출력한다.
"""


def count_ducks(sounds):
    sound_dict = {"q": 0, "u": 0, "a": 0, "c": 0, "k": 0}
    prev_sound = {"q": "k", "u": "q", "a": "u", "c": "a", "k": "c"}

    for sound in sounds:
        if sound_dict[prev_sound[sound]]:
            sound_dict[prev_sound[sound]] -= 1
        elif sound == "q":
            pass
        else:
            return -1

        sound_dict[sound] += 1

    num_ducks = sound_dict.pop("k")

    if sum(sound_dict.values()):
        return -1
    else:
        return num_ducks


if __name__ == "__main__":
    for sound in [
        "quqacukqauackck",
        "kcauq",
        "quackquackquackquackquackquackquackquackquackquack",
        "qqqqqqqqqquuuuuuuuuuaaaaaaaaaacccccccccckkkkkkkkkk",
        "quqaquuacakcqckkuaquckqauckack",
        "quackqauckquack",
    ]:
        print(count_ducks(sound))

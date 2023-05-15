import itertools

def 완주하지_못한_선수(participant, completion):
    player = dict() # 모든 참여선수를 담을 딕셔너리 생성
    participant.sort() # 정렬

    # for i in participant: # 참여 선수 순회
    #     if i not in player.keys(): # 해당 선수 없을 경우
    #         player[i] = 1 # value 를 1로 / key error 방지
    #     else: # 중복 선수 검증
    #         player[i] += 1 # 해당 key 에 1 증감
    for i in participant:
        player[i] = player.get(i, 0) + 1

    for i in completion: # 완주 선수 순회
        player[i] -= 1 # 완주 선수에 해당되는 key 에 value -1 증감

    # 전제 조건이 완주하지 못한 선수는 단 한명이었기 때문에 별다른 조건식 없이 value 가 1일 경우 그 선수가 완주하지 못한 선수이므로 문자열 리턴
    return [key for key, value in player.items() if value == 1][0]

print(완주하지_못한_선수(['leo', 'dasd'], ['leo']))

# def 완주하지_못한_선수_해쉬(participant, completion): # Hash Table Solution (해쉬 테이블 문제)

def 빨간색_초록색_방울(bell):
    coors_start = {}
    coors_end = {}
    for i, x in enumerate(itertools.accumulate([0] + [-1 if b == 1 else 1 for b in bell])):
        if x not in coors_start:
            coors_start[x] = i
        coors_end[x] = i
    return max(coors_end[x] - coors_start[x] for x in coors_end)

# print(빨간색_초록색_방울([1,2,1,1,1,2,2,1]))
# print(빨간색_초록색_방울([2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1]))

# def 체육복(): # Greedy Solution (그리디 문제)



def 가장_큰_수(numbers):
    result = list()

    a = sorted(map(str, numbers), key=lambda x : x*2, reverse=True)
    print(a)
    # numbers.sort(key=lambda x:x*3,reverse=True)


    # k = len(numbers)
    # a = list(itertools.permutations(numbers, len(numbers)))

    # for i in numbers:
    #
    # print(result)

    # return ''.join(result)


# print(가장_큰_수([6, 10, 2, 23, 2, 24]))
# print(가장_큰_수([3, 30, 31, 34, 5, 9, 354]))

# a = ['31', '3', '34']
# a.sort()
# print(a)

a = 0.00

print(str(a))
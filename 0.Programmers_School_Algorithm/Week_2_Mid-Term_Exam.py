#(1)지문 이해 및 풀이 계획
#Merge Sort와 비슷한 느낌으로 구현해주시면 됩니다. string의 시간을 적절히 숫자로 바꿔주는 작업이 필요합니다. 필수로 필요하진 않지만 예외처리를 줄이기 위해 booked/unbooked 끝에 dummy data를 추가하였습니다.

def parse_time(t):
    h, m = map(int, t.split(':'))
    return 60 * h + m


def solution_1(booked, unbooked):
    booked = [(parse_time(t), name) for t, name in booked] + [(1000000, None)]
    unbooked = [(parse_time(t), name) for t, name in unbooked] + [(1000000, None)]
    booked.sort()
    unbooked.sort()
    b, u, t, answer = 0, 0, 0, []

    while b < len(booked) and u < len(unbooked):

        t1, t2 = booked[b][0], unbooked[u][0]
        if t1 <= t:
            answer.append(booked[b][1])
            b += 1
            t += 10
        elif t2 <= t:
            answer.append(unbooked[u][1])
            u += 1
            t += 10
        else:
            t = min(t1, t2)

    answer.pop()
    return answer


# (1)지문 이해 및 풀이 계획
# 작은 사람부터 작은 옷부터 입히면 가장 효율적입니다. 즉, 정렬 후 tshirts을 하나씩 살펴보면서 people보다 크면 입히고, 아니면 넘기면 됩니다. 구현은 이전 문제와 같이 투포인터를 활용하면 됩니다.
def solution_2(people, tshirts):
    people.sort()
    tshirts.sort()
    p, t, ans = 0, 0, 0
    while p < len(people) and t < len(tshirts):
        if tshirts[t] >= people[p]:
            ans += 1
            p += 1
        t += 1
    return ans
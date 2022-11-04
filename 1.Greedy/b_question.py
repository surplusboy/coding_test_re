# 첫째 줄 N, M, K의 자연수
# 둘째 줄 N개의 자연 수

def my_answer():
    n, m, k = [5, 8, 3]
    data = [2, 4, 5, 4, 6]
    result = 0
    flag = 0

    data = sorted(data, reverse=True)[0:2]

    for i in range(m):
        if flag == k:
            result += data[1]
            flag = 0
            continue
        result += data[0]
        flag += 1
    return result


def model_answer():
    n, m, k = [5, 8, 3]
    data = [2, 4, 5, 4, 6]
    result = 0

    data.sort()

    first = data[-1]
    second = data[-2]

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m -= 1
    return result


def model_answer_2(): # 반복문 없이 수열로 처리하기
    n, m, k = [5, 8, 3]
    data = [2, 4, 5, 4, 6]

    data.sort()

    first = data[-1]
    second = data[-2]

    count = int(m/(k+1)) * k # 수열의 수 * 등장 횟수
    count += m % (k+1) # 총 등장 횟수

    result = 0
    result += count * first
    result += (m - count) * second

    return result


print(model_answer_2())

# 첫째 줄 N, K 입력 받기
# N에서 1을 빼고 N을 K로 나눔, 최소 횟수 출력

def my_answer():
    n, k = 25, 5
    result = 0

    while True:
        if n % k != 0:
            n -= 1
            result += 1
        elif n % k == 0:
            n //= k
            result += 1

        if n == 1:
            break

    return result


def model_answer():
    n, k = 25, 5
    result = 0

    while True:
        target = (n//k) * k
        result += (n-target)
        n = target

        if n < k:
            break

        result += 1
        n //= k  # 25, 5, 0

    return result - 1


print(model_answer())



# 숫자가 쓰인 카드 N * M 형태

n, m = map(int, input().split())

a = int
result = 0
for i in range(n):
    data = map(int, input().split())
    min_value = min(data)

    result = max(result, min_value)

print(result)

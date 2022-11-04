# 8 x 8 의 좌표 평면
# 수평으로 두 칸 이동 수직으로 한 칸 or 수직으로 두 칸 이동 수평으로 한 칸
from itertools import *

# print(ord('a'))

input_data = 'a2'

row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

pattern_list = [1,-1, 2,-2]

pattern = list(permutations(pattern_list, 2))

pop_list = list()

for i, data in enumerate(pattern):
    print(data)
    if abs(data[0]) == abs(data[1]):
        pop_list.append(i)

for i in pop_list[-1::-1]:
    pattern.pop(i)

print(pattern)

result = 0

for i in pattern:
    next_row = row + i[0]
    next_column = column + i[1]
    if next_row >= 1 and next_column >=1 and next_row <= 8 and next_column <= 8:
        print(next_column, next_row)
        result += 1

print(result)


def permutation(arr, n): # 재귀적으로 순열 생성
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for result2 in permutation(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + result2]
    return result


# arr = [1, 2, -1, -2]
# print(permutation(arr, 2))
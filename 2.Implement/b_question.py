# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 체크

# 0 ~ 59 에서 15가지 경우의 수
count = 0
for i in range(0, 60):
    if '3' in str(i):
        print(i)
        count += 1

# for j in range(0, 60):
#     for k in range(0, 60):
#         if '3' in str(j) + str(k):
#             count += 1

# for k in range(0, 60):
#     if '3' in str(k):
#         count += 1
print(count)

n = 10
count = 0
result = 0
# input_condition = 2


def model_answer():
    result = 0
    for i in range(0, n+1):
        for j in range(0, 60):
            for k in range(0, 60):
                if '3' in str(i) + str(j) + str(k):
                    result += 1
    return result


def my_answer(): # 재미로 푼거라 test case는 통과할 수 없는 코드임 (예외 상황이 너무 많음)
    count = 0
    a = 15*60+((60-15)*15) # 조건이 5이하 일때는 무조건 이 공식이 성립하게 된다.
    b = 60*60
    for i in range(n+1):
        if str(i) not in '3':
            count += 1

    result = (a*count) + (n+1-count) * b
    return result

print(model_answer())
print(my_answer())
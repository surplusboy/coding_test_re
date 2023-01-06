'''
스택 자료구조를 활용하여 수식의 중위 표기법을 후위 표기법으로 포맷팅 할 수 있다.
중위 표현식 : 연산자가 피연산자들의 사이에 위치
후위 표현식 : 연산자가 피연산자들의 뒤에 위치
[중위] A * B + C 의 식을 [후위] A B * C +
[중위] A + B * C 의 식을 [후위] A B C * +
'''

# 우선 순위 설정
priority = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def postfixConverter(s):
    stack = list()
    result = str()

    for i in s:
        if i.isalpha():
            result += i
            continue

        if len(stack) == 0:
            stack.append(i)
            continue

        if i == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif i == '(':
            stack.append(i)
        elif i in priority:
            if priority[i] == priority[stack[-1]]:
                result += stack.pop()
                stack.append(i)
            elif priority[i] >= priority[stack[-1]]:
                stack.append(i)
            else:
                if len(stack) >= 2:
                    while True:
                        if priority[stack[-1]] >= priority[i]:
                            result += stack.pop()
                        if len(stack) == 0 or priority[stack[-1]] < priority[i]:
                            break
                    stack.append(i)
                else:
                    result += stack.pop()
                    stack.append(i)

    if len(stack) >= 1:
        while len(stack) != 0:
            result += stack.pop()

    return result

print(postfixConverter('(A+B)*(C+D)'))
print(postfixConverter('A*B+C'))
print(postfixConverter("A+B+C"))
print(postfixConverter('(A+B)*(C+D)'))
print(postfixConverter('A+B*C-D'))

# print(bool(s))
# 후위 표기식의 계산

def splitTokens(exprStr:str) -> list:
    tokens = list()
    val = 0
    processing = False

    for i in exprStr:
        if i == ' ':
            continue
        if i.isdigit():
            val = val * 10 + int(i)
            processing = True
        else:
            if processing:
                tokens.append(val)
                val = 0
            processing = False
            tokens.append(i)
    if processing:
        tokens.append(val)

    return tokens

def infixToPostfix(tokens:list) -> list:
    priority = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1
    }

    stack = list()
    result = list()

    for token in tokens:
        if type(token) is int:
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(token)
                continue

            if priority[token] == priority[stack[-1]]:
                result.append(stack.pop())
                stack.append(token)
            elif priority[token] >= priority[stack[-1]]:
                stack.append(token)
            else:
                if len(stack) >= 2:
                    while True:
                        if priority[stack[-1]] >= priority[token]:
                            result += stack.pop()
                        if len(stack) == 0 or priority[stack[-1]] < priority[token]:
                            break
                    stack.append(token)
                else:
                    result += stack.pop()
                    stack.append(token)
    while len(stack) != 0:
        result.append(stack.pop())

    return result

def postfixEval(tokens:list) -> int:
    stack = list()

    for token in tokens:
        if type(token) is int:
            stack.append(token)
        elif token == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif token == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        elif token == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif token == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)

    return stack.pop()

# print(postfixEval(infixToPostfix(splitTokens('1 + 3 + 5 - 3 * 2'))))
print(infixToPostfix(splitTokens("13 * 27 + 36 * 34")))
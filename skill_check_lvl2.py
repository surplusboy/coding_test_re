
# def solution1(s):
#     return ' '.join([str(min(map(int, s.split(' ')))), str(max(map(int, s.split(' '))))])
#
# # print(solution1("1 2 3 4"))
#
# def solution2(s):
#     cnt = 0
#     answer = str()
#     result = list()
#
#     for i in range(1, len(s)+1):
#         for idx, data in enumerate(s):
#             if s[idx+(i-1):idx+i] == s[idx+i:idx+(i+1)]:
#                 cnt += 1
#             else:
#                 if cnt != 0:
#                     answer += str(cnt+1)+data
#                     cnt = 0
#                 else:
#                     answer += data
#         result.append(answer)
#         answer = str()
#     print(answer)
#     print(result)
import re



def solution1(files):
    pattern = re.compile(('\d+'))
    pattern2 = re.compile('[^\d+]')

    sort_list = list()
    for i in files:
        sort_list += [[pattern.findall(i)[0], pattern2.findall(i)[0]]]

    new_sort = [[x, y[1], int(y[0])] for x, y in enumerate(sort_list)]
    print(new_sort)
    new_sort.sort(key=lambda x: (x[1].lower(), x[2], x[0]))

    print(new_sort)
    result = list()
    for i in new_sort:
        result.append(files[i[0]])

    return result

# print(solution1(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution1(['foo010bar020.zip', 'foo011bar020.zip', 'foo090bar010.zip']))
# print(solution1(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))



# print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))





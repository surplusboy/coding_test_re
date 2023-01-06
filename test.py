import os
import pandas as pd
import csv

i = 1

data = [None, 3, 6, 5]

# print(len(L))
left = 2 * i
right = (2 * i) + 1
smallest = i
# vali = [smallest, left, right]
# check = [data[smallest], data[left], data[right]]
# smallest = vali[check.index(max(check))]

# max(L[smallest], L[left], L[right])
# if data[right]:
#     print('true')


# test = []
print(bool([]))

test = [1,2,3,4,5]

stack = []
while test:
    print(test.pop())



# if not not test:
#     print('ture')
# else:
#     print('false')

# L = [[1,2], [2,1], [1,1]]

# L.sort(key = lambda x : (-x[1], x[0]))
# print(L)


def print_ls(path):
    PATH = path

    file_ls = []
    max_depth = 0
    for path, dir, files in os.walk(PATH):
        for file in files:
            current = os.path.join(path, file).replace('\\', '/')
            file_ls.append(current)
            print('/'.join(current.split('/')[4:]))
            # input()

            # if len(current.split('/')) > max_depth:
            #     max_depth = len(current.split('/'))
    # return file_ls

# print(print_ls())

def write_csv(csv_path, max_depth, path):
    PATH = path
    os.chdir(csv_path)
    depth = list(range(0, max_depth, 1))
    with open('folder_data.csv', 'w', newline='', encoding='cp949') as f:
        w = csv.writer(f)
        w.writerow(' '.join(str(e) for e in depth).split())

        for path, dir, files in os.walk(PATH):
            for file in files:
                current = os.path.join(path, file).replace('\\', '/')
                row = os.path.relpath(current, PATH).split(os.sep)
                w.writerow(row)

    df = pd.read_csv('folder_data.csv', error_bad_lines=False, index_col=None,
                     header=0, engine='python', encoding='cp949')
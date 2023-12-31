import sys


def query_point(x, y):
    print("?", x, y)
    sys.stdout.flush()
    response = input().strip()
    return response


def announce_result(result):
    print("!", result)
    sys.stdout.flush()


answers = []
start_coordinate = None
end_coordinate = None

for i in range(1, 101):
    for j in range(1, 101):
        if query_point(i, j) == 'inside':
            start_coordinate = (i, j)
            break
    if start_coordinate:
        break

flag = False
now_i,  now_j = start_coordinate
for i in range(1, 101):
    now_i += 1
    now_j += 1
    if query_point(now_i, now_j) == 'outside':
        end_coordinate = (now_i - 1, now_j - 1)
        flag = True
        break

if flag:
    if query_point(end_coordinate[0], end_coordinate[1] + 1) == 'inside':
        announce_result('rectangle')
    else:
        announce_result('square')


# width = end_coordinate[1] - start_coordinate[1]
# height = end_coordinate[0] - start_coordinate[0]
#
# if width == height:
#     announce_result("square")
# else:
#     announce_result("rectangle")

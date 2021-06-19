import sys


def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solution(l, r):
    if l == r:
        return float('inf')
    else:
        m = (l + r) // 2 #중간 점
        min_dist = min(solution(l, m), solution(m + 1, r))
        target_list = []
        #x축을 기준으로 min_dist보다 작은 점들을 target_list에 추가함.
        #왼쪽
        for i in range(m, l - 1, -1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break
        #오른쪽
        for j in range(m + 1, r + 1):
            if (sorted_location[j][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[j])
            else:
                break
        #이제, 1차로 x축을 기준으로 걸러진 target_list에서 y축을 기준으로 비교해서 가장 작은 값을 찾아냄.
        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_list[i], target_list[j])
                    min_dist = min(min_dist, dist)
                else:
                    break
        return min_dist


n = int(input())
Points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 중복 제거
sorted_location = list(set(map(tuple, Points)))
if len(sorted_location) != len(Points):
    print("0")
else:
    sorted_location.sort()
    print((solution(0, len(sorted_location) - 1)))

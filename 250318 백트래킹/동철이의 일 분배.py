# import sys
# sys.stdin = open("input.txt","r")

def how_tobe_good_worker(row,total_per):
    global greatest_percent
    # 1보다 작은 값에 분수를 곱할 경우 더 작아지기 때문에

    # total_per가 최대값보다 작아지면 더 커질 일이 없으므로 return
    if total_per < greatest_percent:
        return

    # 각 일을 모두 선택했을 때 크기 비교
    if row == N:
        greatest_percent=max(total_per,greatest_percent)
        return

    # 재귀
    for i in range(N):
        if not visited[i]:
            if each_percent[row][i] != 0:
                visited[i] = True
                how_tobe_good_worker(row+1,total_per * each_percent[row][i])
                visited[i] = False




T =int(input())

for tc in range(1,1+T):
    N = int(input()) # 해야할 일의 개수
    each_percent = [list(map(int,input().split())) for _ in range(N)]
    each_percent = [[x / 100 for x in row] for row in each_percent]


    greatest_percent = float('-inf')

    visited = [False] * N # 일을 하나씩 골랐는지
    how_tobe_good_worker(0,1)

    answer = f"{100 * greatest_percent:.6f}"

    print(f"#{tc} {answer}")


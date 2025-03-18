
def good_decision_making(row,total):
    global min_money

    if row == N:
        min_money = min(total,min_money)
        return
    if min_money <= total:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            good_decision_making(row+1,total+expense[row][i])
            visited[i] = False




T = int(input())

for tc in range(1,1+T):
    N = int(input())
    min_money = float('inf')
    expense = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    good_decision_making(0,0)

    print(f"#{tc} {min_money}")
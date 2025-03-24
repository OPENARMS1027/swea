# import sys
# sys.stdin = open("input.txt","r")
from heapq import heappush,heappop

def good_repair(si,sj):
    # 초기값 할당
    heap =[(0,si,sj)]
    D = [[float("inf")] * N for _ in range(N)] #최솟값 할당해줄 리스트
    D[si][sj] = 0

    while heap:
        w,r,c = heappop(heap)

        if r == N-1 and c == N-1:
            return D[r][c]

        if w > D[r][c]: # 방문했거나 최소값 보다 크면은
            continue

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            sum_w = w + land[nr][nc] # 지금까지의 최솟값 + 다음칸 수리비용

            # 만약 다음 칸 갔을 때 같거나 더 크면 최소가 아니라 갈 이유가 없음
            # continue 하고 다음 반복 돌기
            if sum_w >= D[nr][nc]:
                continue
            # 위쪽에 걸리지 않았다면 최소값 이니 그 다음 탐색하게 push
            D[nr][nc] = sum_w # 조건에 걸리지 않았으니 최소값이라 가중치 할당
            heappush(heap,(sum_w,nr,nc))
    

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    land = [list(map(int,input())) for _ in range(N)]

    answer = good_repair(0,0)

    print(f"#{tc} {answer}")

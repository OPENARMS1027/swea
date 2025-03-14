

    
# 이동하는 방의 수가 최대가 되는 출발 방 번호, 최대 이동 가능 방 수 출력

T =int(input())
for tc in range(1,1+T):
    N = int(input()) # NxN 방 
        
    # 각 위치에서 1만큼 차이나는 방이 주변에 있을 때 이동 가능
    # 각 방에서 갈 수 있는 방의 유무를 체크해준다면 이어서 방을 이동할 수 있는
    # 최대 횟수를 구할 수 있다.
    rooms = [list(map(int,input().split())) for _ in range(N)]
    max_counts = float("-inf") # 최대 이동 방 개수 출력

    arrived = [0] * (N*N+1) # 각 지점에서 다음 방문할 곳이 있는지 여부 체크

    # 행,열 순회하며 갈 수 있는 곳이 있다면 체크해주기
    for r in range(N):
        for c in range(N):
            for dr,dc in ([0,1],[1,0],[0,-1],[-1,0]):
                nr = r + dr
                nc = c + dc
                # 갈 수 있는 곳이 있다면 1로 체크
                if 0<=nr<N and 0<=nc<N and rooms[nr][nc] - rooms[r][c] == 1:
                    arrived[rooms[r][c]] = 1
                    break

    # 단순히 최대 길이를 구하려면 count만 세어줘도 된다.
    # 만약 다른 문제에서 반전동작이 필요하거나, 특정 조건을 만족하는 구간 찾거나, 이전 상태를 고려해야 할 때
    # 상태를 나타내는 변수를 사용해야 한다.
    count = start = 0
    for i in range(1,N*N+1):
        if arrived[i] == 1:
            count += 1
        
        else:
            if max_counts < count:
                max_counts = count
                start = i - count
            count = 0


    # 갈 수 있는 여부니까 마지막 idx요소에서 +1 해줘야 총 갈 수 있는 방의 개수
    print(f"#{tc} {start} {max_counts+1}")
# 백트랙킹 함수 (재귀)
# 현재 내가 몇칸 갈지 선택하고 있는 정류장 번호 : idx
def backtracking(idx,cnt):
    global min_count
    # 1. 종료조건 : 목적지에 도착했을 때

    if min_count <= cnt:
        return
    if idx >= N - 1:
        # 마지막 정류장에 도착하거나 재껴버리면(재낀것도 도착하고간거)
        # 지금까지 충전한 횟수가 최소 충전 횟수인지 확인
        min_count=min(cnt,min_count)
        return

    # 2. 재귀호출(경우의 수 나열하고 선택)
    # idx 번의 충전 용량2
    # 다음에 갈 수 있는 정류장 번호 ㅣ idx +1, idx +2 ... bus_stop[idx]

    # 현재 위치에서 최대 용량만큼 먼저 가보고 그 다음에 1씩 줄여서 이동
    for i in range(bus_stop[idx],0,-1):
        # 이동하는 정류장 개수 i
        backtracking(idx+i,cnt+1)

T = int(input())

for tc in range(1,1+T):
    bus_stop = list(map(int,input().split())) + [0]
    N = bus_stop.pop(0)

    min_count = float('inf')
    backtracking(0,0)  # or backtracking(0,-1) 둘의 차이는 처음껄 빼줬냐 안 빼줬냐
    min_count -= 1 # 처음거 빼주기, 위 코드에서는 처음걸 카운트 해줬음
    # 주석 처리처럼 할 시 처음에 빼주고 시작하기 때문에 문제 없음
    print(f"#{tc} {min_count}")


from collections import deque

def bfs(start):
    # bfs에 사용할 큐
    q = deque() # 빈 덱 생성
    # 내가 이전에 만든 숫자를 또 만들지 않도록 중복체크
    # v = [0] * (1000000+1)
    v = set()
    # 시작 숫자 중복 체크
    v.add(start)
    # 큐에 시작 숫자를 넣고
    # 연산 횟수(0)도 같이 넣어주기
    q.append((start,0))

    # 탐색
    while q:
        # 큐에서 하나 꺼내오기
        # num 숫자를 만들기 위해 최소 연산 cnt번 했다.
        num, cnt = q.popleft()

        if num == M:
            return cnt

        # num 숫자에 할 수 있는 연산은
        # +1, -1, *2, -10
        # 연산 결과를 next_num이라고 하자
        for next_num in (num+1,num-1,num*2,num-10):
            # next_num이 가능 ?
            # 문제 범위 내인가
            # 이전에 만든적이 없는가
            # 위 조건을 만족시 연산 이어나가기 가능
            if 1 <=next_num <= 1000000 and next_num not in v:
                # 범위안이고, 이전에 만든적 없으니 계속해서 진행
                # 중복 체크
                v.add(next_num)

                q.append((next_num, cnt+1))



T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())  # 자연수 N에 몇 번의 연산을 통해 만들어줄 다른 자연수 M
    # N을 M으로 만들려면 최소 몇번의 연산을 해야하는가 ?
    answer = bfs(N)
    print(f"#{tc} {answer}")

T = int(input())

for tc in range(1,1+T):
    a, b, c = map(int,input().split())

    answer = -1 # 불가능하다고 가정

    # 가능할 때는 
    if a>0 and b>1 and c>2: # 0이 되면 안되고 크기는 순서대로 되어야하므로
        # c가 엄청 크면 조건에 성립. 따라서 c는 그대로 놔두고 a,b를 조정해준다.
        # b는 c보다 1만 작으면 성립하고 a는 그 작아진 b보다 1만 작으면 성립
        # b가 c와 같거나 클 때
        answer = 0 # 기본 값 0 할당
        if b >= c:
            answer += b-(c-1) # 빼줄 b값 더해주기
            b = c-1 # a와 비교해야해서 b값 재할당
        
        # a가 b와 같거나 클 때, b보다 작을 때는 조건에 부합
        if a >= b:
            answer += a-(b-1) # a는 b보다 1만 작으면 성립(최소값을 빼줄 수 있음)

    print(f"#{tc} {answer}")

        
    
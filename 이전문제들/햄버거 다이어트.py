
# 인덱스 요소, 점수, 칼로리 파라미터 사용
def making_burger(idx,now_score,now_kcal):
    global max_score

    if now_kcal <= L: # 조합했을 때 칼로리가 기준보다 낮을 때
        if max_score < now_score: # 만족도 확인 후 최신화
            max_score = now_score

    else: # 칼로리 넘었다면 return
        return
    
    if idx == N: # 재료 다 썼으면 return
        return
    
    # 리스트에서 꺼내올거기 때문에 따로 변수 할당
    score = hopes[idx]
    kcal = calories[idx]
    
    # 재료 선택했을 때와 선택하지 않았을 때
    # 다음 재료로 넘어가기 위해 idx 변경
    # 선택시 칼로리와 스코어 추가
    # 선택하지 않았을 때 score와 kcal는 그대로 넘겨줌
    making_burger(idx+1, now_score+score,now_kcal+kcal)
    making_burger(idx+1, now_score,now_kcal)

    
    
T = int(input())

# 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거 점수 출력
for tc in range(1,1+T):
    # N개의 재료 수, L까지의 제한 칼로리
    N, L = map(int,input().split())
    max_score = 0

    # 리스트 사용했기에 인덱스를 변경하면서 확인해줄 필요가 있음
    hopes = []
    calories =[]
    
    for _ in range(N):
        # 맛에 대한 점수, 칼로리
        a,b = map(int,input().split())
        hopes.append(a)
        calories.append(b)
    
    making_burger(0,0,0)
    print(f"#{tc} {max_score}")


        




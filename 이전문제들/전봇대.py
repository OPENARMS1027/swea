T = int(input())

for tc in range(1,1+T):
    N = int(input())

    a_lst =[] # 왼쪽 전봇대에서 전깃줄 높이
    b_lst =[] # 오른쪽 전봇대에서 전깃줄 높이
    x_point = 0 # 교차점 세 줄 리스트

    for _ in range(N): # 반복문 돌아가며 a,b를 할당받아 리스트에 저장
        a,b = map(int,input().split())
        a_lst.append(a)
        b_lst.append(b)

    # i번째 줄과 다른 줄들을 하나하나 비교
    for i in range(N-1): # 끝까지 비교하기 위해 인덱스 조정
        for k in range(i,N-1): # i전깃줄과 그 다음 전깃줄을 비교
            # 교차점이 생기는 경우는 x자를 그릴 때이므로 그 때의 조건이
            # 두 개의 전깃줄 중 하나의 전깃줄 시작점이 그 다음 전깃줄 시작점보다 낮고 끝점은 반대일 때
            # 그리고 둘다 반대일 때
            if a_lst[i] < a_lst[k+1] and b_lst[i] > b_lst[k+1] or a_lst[i] > a_lst[k+1] and b_lst[i] < b_lst[k+1]:
                x_point += 1 # 교차점 추가
    
    print(f"#{tc} {x_point}")





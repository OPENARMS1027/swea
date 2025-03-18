
T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # N,M 각 배열의 숫자 개수
    a = list(map(int,input().split()))
    a.sort()
    b = list(map(int,input().split()))

    # b에 있는게 a에도 있는 수들 중에
    count = 0 # 중간값을 원하거나, 왼쪽 오른쪽을 다 검색하는 경우 카운트

    a_left = 0 # 좌우 값 
    a_right = N - 1
    
    idx = 0 # b배열 차례대로 볼 idx
    l_check = r_check = 0 # 양쪽 다 확인 했는지 

    # 다 봤으면 종료
    while idx < M:
        mid = (a_left + a_right) // 2
        # b값을 순서대로 a에 있는지 확인하려고 한다
        # a 리스트의 좌우값을 바꿔주며 확인

        # 바로 중간값이면 count + 1
        if a_left == 0 and a_right == N - 1:
            if a[mid] == b[idx]:
                count += 1 # 세주고
                idx += 1 # 다음거 넘어가고
                continue

        # b값이 a에 있고 좌우 한번씩 봤으면
        # 세주고, 다음거 넘어가고, 여부 초기화, 위치 초기화
        if a[mid] == b[idx]: 
            if l_check and r_check or not l_check and r_check == 1 or not r_check and l_check == 1:
                count += 1 
            idx += 1
            l_check = r_check = 0
            a_left = 0
            a_right = N - 1
            continue

        # 아니면 이진탐색 
        if b[idx] < a[mid]:
            a_right = mid - 1
            l_check += 1
        elif b[idx] > a[mid]:
            a_left = mid + 1
            r_check += 1

        # 왼쪽값이 더 커지면 없는거
        # 다음거 넘어가고, 여부 초기화, 위치 초기화
        if a_left > a_right:
            idx += 1
            l_check = r_check = 0
            a_left = 0
            a_right = N - 1
            continue

    print(f"#{tc} {count}")


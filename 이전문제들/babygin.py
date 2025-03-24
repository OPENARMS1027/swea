
# 연속인 숫자 3개 이상인지 확인하는 함수
def check_succesive(arr,point):
    arr.sort()
    arr = set(arr)
    arr = list(arr)
    if len(arr) >= 3:
        for c in range(len(arr)-2):
            if arr[c+1] - arr[c] == 1 and arr[c+2] - arr[c+1] == 1:
                return point + 1
    return point


# 같은 숫자가 3개 이상인 triplet 인지 확인하는 함수
def three_same_num(n,arr,point):
    arr.sort()
    for a in range(n):
        cnt = 1
        for k in range(a+1,n):
            if arr[a] == arr[k]:
                cnt += 1
            if cnt == 3:
                return point +1
    return point



T = int(input())

for tc in range(1,1+T):
    num_lst = list(map(int,input().split()))

    p1 = [] # 플레이어 1이 가져간 카드
    p2 = [] # 플레이어 2가 가져간 카드
    win_point_1 = 0
    win_point_2 = 0
    answer = 0  # 무승부라 가정

    for i in range(6):
         p1.append(num_lst[2*i])
         p2.append(num_lst[2*i+1])

         if i >= 2: # 3개 이상 되었을 때 검사
            win_point_1 = check_succesive(p1,win_point_1)
            win_point_1 = three_same_num(i + 1, p1, win_point_1)
            if win_point_1 > win_point_2:
                answer = 1
                break

            win_point_2 = check_succesive(p2,win_point_2)
            win_point_2 = three_same_num(i+1,p2,win_point_2)
            if win_point_1 < win_point_2:
                answer = 2
                break


    print(f"#{tc} {answer}")
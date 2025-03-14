T = int(input())

def same_sum_counting(idx,arr,sum):
    global counts
    if sum == K:
        counts += 1
        return
    if idx >= N:
        return

    num = num_lst[idx]
    same_sum_counting(idx +1,arr,sum + num) # 선택 하는 경우
    same_sum_counting(idx +1,arr,sum) # 선택 안 하는 경우





for tc in range(1,1+T):
    N, K = map(int,input().split()) # N개의 자연수, 합이 K가 되는 경우의 수
    num_lst = list(map(int,input().split())) # N개의 자연수
    counts = 0
    same_sum_counting(0,num_lst,0)

    print(f"#{tc} {counts}")


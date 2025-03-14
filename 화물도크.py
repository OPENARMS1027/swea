T = int(input())
def checking(arr,a,c): # 리스트 체크하는 함수
    global counts
    while c < N: # 마지막 요소까지 비교하기
        if arr[a][1] <= arr[c][0]: # 시작시간과 종료시간 비교하기
            counts += 1
            a = c # 맞다면 계속해서 비교해주기 위해 뒷 작업으로 넘어가기
        c += 1 # 앞 작업과 뒷 작업이 이어서 가능하든 안 하든 다음거 확인




for tc in range(1,1+T):
    N = int(input())

    counts = 1 # 작업 몇개 가능한지 세 줄 변수, 시작거 안 세기 때문에 1
    time_lst=[] # [시작시간,종료시간]을 저장해줄 함수
    # N개의 인풋
    for _ in range(N): 
        # 작업 시작 시간 s, 종료 시간 e가 주어진다.
        s, e = map(int,input().split())
        time_lst.append([s,e])
    
    # 작업 끝나는 시간 빠른 기준으로 정렬
    time_lst.sort(key=lambda x:x[1])
    # 리스트 체크하기
    checking(time_lst,0,1)

    print(f'#{tc} {counts}')
        
    


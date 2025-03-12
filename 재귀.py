T = int(input())

# 가지치기 추가해줌 
def add_board(i,j,total):
    global total_boards
    if total_boards < total:
        return
    if i>= N or j >= N: # 종점 벗어나면 종료
        return
    
    total += boards[i][j]

    if i==j==N-1: # 종점일 때
        if total_boards > total: # 최솟값 할당
            total_boards = total
            

    
    # check_lst[i][j] = 1
    add_board(i+1,j,total)
    add_board(i,j+1,total)
    
    

for tc in range(1,1+T):
    N = int(input())

    boards = [list(map(int,input().split())) for _ in range(N)]
    total_boards = float('inf') # 더해준 값을 할당해 줄 변수
    # check_lst = [[0] * N for _ in range(N)]
    add_board(0,0,0)

    print(f"#{tc} {total_boards}")

    
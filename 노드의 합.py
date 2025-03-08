T = int(input())

# N를 넣어 아래에서 위로 값을 더해나가는 함수 형성
def store_values(leaf):
    for i in range(leaf,1,-1):
        nodes_value[i//2] += nodes_value[i]

for tc in range(1,1+T):
    # N개의 노드 개수, 리프 노드 개수 M, 값 출력할 노드 번호 L
    N, M, L = map(int,input().split())

    # 값 저장해줄 리스트
    nodes_value = [0] * (N+1)

    # 리프 노드 번호와 1000이하의 자연수 input
    # 노드 값 리스트에 값 넣어주기
    for _ in range(M):
        leaf_num, leaf_value = map(int,input().split())
        nodes_value[leaf_num] = leaf_value
    
    store_values(N)
    print(f"#{tc} {nodes_value[L]}")   


    

    
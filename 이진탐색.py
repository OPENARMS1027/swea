T = int(input())

# 주어진 N으로 만들어진 완전 이진 트리의 탐색
# 루트에 저장된 값, N/2번 노드에 저장된 값 출력하는 프로그램
# 중위 탐색 순서로 값이 커지는 규칙을 가짐

# 자식 값 인덱스에 값을 넣어줄 함수 생성
# 루트 idx는 1
# 
def push_value(num):   
    global value 
    if num <= N:
        push_value(2*num)
        values_tree[num] = value
        value += 1 
        push_value(2*num+1)

for tc in range(1,1+T):
    N = int(input()) # 1부터 N까지의 자연수
    value = 1
    values_tree = [0] * (N+1) # 노드의 값 넣어줄 리스트
    
    push_value(1)

    print(f"#{tc} {values_tree[1]} {values_tree[N//2]}")
    
        
    


    

    

    
    


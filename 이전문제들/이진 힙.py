T = int(input())

# 최소합에 enq 해주는 함수 생성
def enq(a):
    global last
    last += 1
    heap[last] = a # 마지막 인덱스(정점)에 값 추가해주기

    c = last # last값 따로 할당해줘서 last값 영향주지 않고
    # 값 비교하기
    p = c // 2 # enq해주는 값 정점의 부모 정점 번호
    # 부모가 존재하고 부모가 자식값보다 더 크다면
    while p and heap[p] > heap[c]: 
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

for tc in range(1,1+T):
    # 주어지는 N개의 서로 다른 자연수 
    N = int(input()) # 서로 다른 N개의 자연수가 주어진다.
    values  = list(map(int,input().split())) # 값 input
    last = 0 # enq할 때 정점 위치로 써 줄 변수
    
    # 값 넣어줄 리스트 생성, 리스트에 값 넣어주기
    heap = [0] * (N+1) 
    sum_values = 0 # 조상 value 추가해줄 함수

    # 최소힙 삽입 함수 실행   
    for c in values:
        enq(c)
    
    
    # 마지막 노드의 조상 노드에 저장된 정수의 합 알아내기
    sum_values = 0 # 값 더해줄 변수

    while N > 1:
        
        sum_values += heap[N//2]
        N = N // 2
    
    print(f"#{tc} {sum_values}")

    # # 삭제라면 ?
    # def deq(): # 삭제는 루트값만 가능함, 
    #     # 다른 값을 삭제한다면 빈 공간이 생겨서 구조가 깨지기 때문
    #     # 따라서 (1)삭제 후 (2)마지막 노드를 루트로 올려서 재정렬 하는 방법 사용
    #     global last
    #     tmp = heap[1] # root 값 백업 return은 루트
    #     heap[1] = heap[last] # 삭제할 노드의 키 루트에 복사
    #     # enq에서 값 추가하고 항상 last값으로 위치 최신화해줬으므로
    #     # 마지막 추가해준 값의 위치 last
    #     last -= 1  # 인덱스 줄여즘으로써 마지막 노드 값 다루지 않음(삭제)
        
    #     # (pre (2)) 재정렬 전에 값 비교
    #     p = 1
    #     c = p * 2
    #     while c <= last: # 자식이 하나라도 있으면
    #         # 만약 오른쪽 자식이 있고 오른쪽 자식이 더크면
    #         if c+1 <=last and heap[c] < heap[c+1]:
    #             c += 1 # 오른쪽 자식으로 비교대상 정함
    #             # c +=1 해줌으로써 타깃 오른쪽 자식변경
    #         # 오른쪽 자식보다 부모가 크다면 둘 변경    
    #         if heap[p] > heap[c]: # 값 변경
    #             heap[p], heap[c] = heap[c],heap[p]
    #             # 다음 단계의 반복을 위한 설정
    #             p = c # 자식을 새로운 부모로 
    #             c = p*2 # 자식 재설정
    #         else: # 부모 값이 더 크면 정상이니까 반복문 종료
    #             break 
        
    #     return tmp # deq해준 root값 반환
    #     # root값만 제거 가능함으로 

        
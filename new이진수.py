T = int(input())

def solution():
    mask = (1 << N) - 1 # 이 식을 이용하면 2진법으로 바꿨을 때 N개의 비트가 모두 1을 가진 이진수 생성
    if (M & mask) == mask: # 만약 주어진 M이 그 수와 AND 연산자 사용했을 때 mask와 같다면
        return 'ON'
    return 'OFF'


for tc in range(1,1+T):
    # 정수 M을 이진수 표현했을 때, 마지막 N 비트가 모두 1로 켜져있는지 출력
    N,M = map(int,input().split()) 
    
    # status = 'ON' # 기본 상태 ON으로 가정
    # status = 'OFF'
    # N만큼 반복해서 정수 M을 이진수로 바꿨을 때 N개의 비트 확인하기 
    # for i in range(N):
    #     # 비트 연산자 이용
    #     # M의 i번째 요소가 1인지 확인
    #     if M & 1 != 1:
    #         status = 'OFF'
    #         break
    #     M = M >> 1
    #
    # print(f"#{tc} {status}")


    solution()
    print(f"#{tc} {solution()}")







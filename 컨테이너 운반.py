T = int(input())
# 트럭 리스트, 적재 무게 리스트 비교하기
def checking(arr1,arr2,a,b):
    global answer
    while a < M and b < N:
        if arr1[a] >= arr2[b]:
            answer += arr2[b] # 무게 추가
            a += 1
            b += 1
        else:
            b += 1
    
    
for tc in range(1,1+T):
    N, M = map(int,input().split()) # N개화물, M대 트럭
    # 화물 무게 리스트
    baggage = list(map(int,input().split()))
    # M개 트럭의 가능 적재용량 리스트
    max_ton = list(map(int,input().split()))

    answer = 0 # 최대 적재 무게

    # 내림차순으로 두 리스트 정렬
    baggage.sort(reverse=True)
    max_ton.sort(reverse=True)

    checking(max_ton,baggage,0,0)

    print(f"#{tc} {answer}")
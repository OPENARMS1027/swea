def finding_best_route(arr,):
x



T = int(input())
for tc in range(1,1+T):
    N = int(input()) # 카페 지역의 한 변의 길이 N

    # 카페 디저트 종류별 번호    
    cafes = [list(map(int,input().split())) for _ in range(N)]
    max_dessert = float("-inf")

    

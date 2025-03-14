
def make_tower(arr,idx,total):
    global min_height
    if total >= B: # 키를 합친 값이 B를 넘었다면 굳이 다음걸로 넘어가서 더해줄 필요가 없음
        if min_height > total:
            min_height = total
        return total
    if idx >= N: # 다 결정했을 때 return
        return total
    inch = arr[idx]
    make_tower(arr, idx + 1, total) # 포함 안 할 때
    make_tower(arr, idx + 1, total + inch) # 포함 할 때

T = int(input())
for tc in range(1,1+T):
    N, B = map(int,input().split()) # N명의 점원, 높이가 B인 선반
    height = list(map(int,input().split())) # 키 리스트
    min_height = float('inf')
    # 탑의 높이와 B의 차이가 가장 작은 것을 출력한다.

    make_tower(height,0,0)
    print(f"#{tc} {min_height - B}")





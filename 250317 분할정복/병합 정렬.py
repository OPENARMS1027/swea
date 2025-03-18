def merge(left,right):
    global count
    # 최종적으로 정렬한 결과 담을 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0 # 왼쪽 오른쪽 리스트의 각각의 인덱스
    if left[-1] > right[-1]:
        count += 1

    # 왼쪽, 오른쪽 리스트가 빌떄까지 계속 비교하면서 결과 리스트에 추가
    # 더 작은 값을 우선적으로 넣어주며 0에서 시작한 l과 r값으로 인덱싱
    
    while l <len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] =right[r]
            r += 1
    # l값이 남았다면(인덱스가 끝까지 가지 않았다면)
    while l < len(left):
        result[l+r] = left[l] #추가
        l += 1 # 인덱싱
    # r값이 남았다면(인덱스가 끝까지 가지 않았다면)
    while r < len(right):
        result[l+r] = right[r]
        r += 1
    
    return result 




# 리스트를 분할했다가 병합해준다.
def merge_sort(li):
    if len(li) == 1: # 리스트의 길이가 1개가 되면 return, # 재귀를 통해 모든 리스트의 길이가 1이된다.
        return li
    
    mid = len(li) // 2
    left = li[:mid] 
    right = li[mid:]

    # 왼쪽,오른쪽으로 나눠준 리스트를 계속해서 재귀 
    # merge_sort 함수에서 길이가 1이 될떄까지 분할
    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # 분할해줬기에 병합하면서 정렬해 나간다
    merge_list = merge(left_list,right_list)
    return merge_list





T = int(input())

for tc in range(1,1+T):
    N = int(input())
    lst = list(map(int,input().split()))
    count = 0

    a = merge_sort(lst)
    print(f"#{tc} {a[N//2]} {count}")


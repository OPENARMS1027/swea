

def partition(left,right):
    pivot = lst[left]
    i = left + 1
    j = right

    # i가 j와 같거나 작을 때
    # 여기서 좌우가 나누어졌을 때 i(left +1)가 j(right)값 보다 커지는 것은
    # 리스트의 길이가 1개가 되었을 때 
    # 조건 검사와 swap과정을 여러번 반복하기 위한 While문
    while i <= j:
        # 두 인덱스를 i는 오른쪽, j는 왼쪽으로 가며 pivot의 위치를 찾아주는것
        # 왜 ? -> 피봇의 위치를 잡아서 좌우로 나눠주기 위해서
        # 피봇보다 큰 값을 찾아나가면서 오른쪽으로 진행
        while i <= j and lst[i] <= pivot:
            i += 1 # 오른쪽으로 이동
        # 피봇보다 작은 값을 찾아나가면서 왼쪽으로 진행
        while i <= j and lst[j] >= pivot:
            j -= 1 #왼쪽으로 이동
        
        # swap 해준다.
        # 만약 i와 j가 교차한다면 두 인덱스 표시는 분할의 경계(pivot위치)를 넘었기 때문에
        # 이 경우에는 올바른 교환이 이뤄지지 않음
        # 즉 유효한 위치에서만 교환
        if i < j:
            lst[i], lst[j] = lst[j],lst[i]

    lst[left], lst[j] = lst[j], lst[left]
    return j # pivot의 위치를 quick_sort 함수에 return 해주면서 재귀

def quick_sort(left,right):
    if left < right:
        # pivot 기준으로 정렬시킴
        pivot = partition(left,right)        
        quick_sort(left,pivot-1)# 왼쪽 부분 진행
        quick_sort(pivot+1,right)# 오른쪽 부분 진행


T = int(input())

for tc in range(1,1+T):
    N = int(input()) # 정수의 개수 N
    lst = list(map(int,input().split()))
    quick_sort(0,N-1) # 함수 실행

    answer = lst[N//2]
    print(f"#{tc} {answer}")


    
# 각 집합을 만들어 준다잇
def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents,ranks

# 두개를 같은 집합으로 만들기

def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x ==ref_y:
        return
    
    # 어디껄 기준으로 할지는 선택사항
    # 이 코드는 rank가 작은 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    
    else: # rank 같으면 한쪽으로 병합하고 대표자의 Rank 증가시켜줌
        parents[ref_y] = ref_x
        ranks[ref_x] += 1
    

# 부모를 타고 가서 대표자를 찾아간다.
# 찾아가서 리스트의 값을 대표로 바꾸는 과정
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]
        

T = int(input())

for tc in range(1,1+T):
    # 1번부터 N번까지의 출석번호가 있고
    # M장의 신청서가 제출 된다
    N,M = map(int,input().split())
    parents,ranks = make_set(N)
    #관계를 리스트로 input
    relations = list(map(int,input().split()))
    
    # 받은 관계를 같은 집합으로 만들어준다.
    for i in range(0,2*M,2):
        union(relations[i],relations[i+1])
    # 부모를 안겹치게 들어가도록 set에 넣어줌
    answer = set()
    '''
    union함수를 실행시킨 원소들은 같은 집합에 넣어줬지만
    실행되면서 같은 집합에만 들어가고 대표자가 변경되지 않은 경우가 발생할 수 있다.
    따라서 단순히 부모 리스트의 값들을 set에 추가해주는 것이 아니라
    하나하나 대표자를 찾은 뒤 추가해줘야 함 
    '''
    for i in range(1,N+1):
        answer.add(find_set(i))

    print(f"#{tc} {len(answer)}")
    
    
    

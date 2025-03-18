class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key


# 1. 탐색
# root : 찾기 시작하는 트리의 루트 노드
# key : 우리가 트리 안에서 찾으려고 하는 값
# 루트와 키가 같으면 탐색 성공
# 작다면 루트 노드의 왼쪽 탐색
# 크다면 루트 노드의 오른쪽 탐색

def search(root,key):
    # root가 없다면 탐색실패

    # root에서 탐색 실패 했다 라는 것을 알려주기 위해 return root

    # 내가 찾는 값 key가 루트노드의 key와 같다면 탐색 성공
    if root is None or root.value == key:
        return root
    # 내가 찾는 값 key가 루트노드의 key보다 작다면 루트노드의 왼쪽을 다시 탐색
    if key < root.value:
        return search(root.left,key)
    # 내가 찾는 값 key가 루트노드의 key보다 크다면 루트노드의 오른쪽을 다시 탐색
    if key > root.value:
        return search(root.right,key)


# 2. 삽입 연산
# root : 이진탐색트리의 루트 노드
# key : 내가 삽입하려는 값
def insert(root,key):
    # 트리가 비었을 때 삽입
    if root is None:
        return TreeNode(key)
    else:
        # key와 root의 value 비교
        # 작으면 왼쪽으로
        if key < root.value:
            root.left = insert(root.left, key)

        # 크면 오른쪽으로
        else:
            root.right = insert(root.right, key)

    return root

arr = [8,3,10,2,5,14,11,16]
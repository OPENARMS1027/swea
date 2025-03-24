import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    food_chemistry = [list(map(int,input().split())) for _ in range(N)]

    # 조합 ?
    for i in range(1 << N):
        
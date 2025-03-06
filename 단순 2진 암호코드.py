T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split()) # 배열의 세로크기 N, 배열의 가로크기 M

    arr = [list(map(str,input())) for _ in range(N)]
    secret_num = { '0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4', '0110001':'5' ,'0101111':'6' , '0111011':'7' ,'0110111':'8' ,'0001011':'9'}

    full_secret = '' # 암호 코드

    # 암호 코드 위치 찾기 (끝위치로 찾기)
    for r in range(N):
        for c in range(M-1,-1,-1):
            if arr[r][c] == '1':
                s_i = r
                s_j = c
                break

    for c in range(s_j-55,(s_j+1),7):
        temp =''
        for j in range(c,c+7):
            temp += arr[s_i][j]
        full_secret += temp

    # print(full_secret)
    # 01110110110001011101101100010110001000110100100110111011

    # 암호 코드 숫자들로 바꿔줄 리스트
    real_secret = ''
    # 암호 숫자로 바꿔주기
    for i in range(0,len(full_secret),7):
        if full_secret[i:i+7] in secret_num:
            real_secret += secret_num[full_secret[i:i+7]]

    # print(real_secret)
    # 리스트로 바꿔서 계산쉽게
    judge_list = list(map(int,real_secret))

    answer = sum(judge_list) # 숫자들 합

    # 암호 올바름 판단 과정

    odd = 0 #홀수합
    even = 0 #짝수합
    for i in range(4):
        odd += judge_list[2*i+1] # 인덱스로는 홀수지만 짝수번째 숫자
        even += judge_list[2*i] # 인덱스로는 짝수지만 홀수번째 숫자

    # 올바름 판단
    if ((even *3) + odd) % 10 != 0:
        answer = 0


    print(f"#{tc} {answer}")




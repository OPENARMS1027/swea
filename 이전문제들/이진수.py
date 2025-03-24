T =int(input())

for tc in range(1,1+T):
    N, sixteen_num = input().split() # 문자열 형태로 받음
    hexadecimal = '0123456789ABCDEF'

    full_length_str = ''
    for i in range(int(N)): # 문자를 순회하면서 2진법으로 바꿔주기
        two_str =''
        for j in range(16): # 16진수의 형태와 같은지 확인
            if sixteen_num[i] == hexadecimal[j]: # 입력 받은 문자가 같다면
                # 비트 연산자로 확인
                for a in range(3,-1,-1): # 2진수로 표현하면 4자리니까 앞에서부터 각 자리를 확인
                    # j를 2진수로 표현했을 때(비트의 형태) a만큼 밀었을때
                    if 1 & (j >> a):
                        two_str += '1'
                    else:
                        two_str += '0'
        full_length_str += two_str

    print(f"#{tc} {full_length_str}")












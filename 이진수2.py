# 수를 이진수로 표현했을 때 13자리 이상이라면 overflow 출력
# 넘지 않으면 0. 을 제외한 나머지 숫자 출력

T=int(input())

for tc in range(1,1+T):
    N = float(input()) # 수 N
    
    decimal = '' # 13미만일때 출력해줄 수
    x = 1 # 시작 소수점 자리 수

    while True:
        if N >= 2**(-x): # 더 작으면 
            N = N - 2**(-x) # 값만큼 빼주고 변수에 재할당
            decimal += '1' # 소수점 수 답에 추가해주기
            if N == 0: # 만약 끝났다면
                break

        # 더 크다면 
        else:
            decimal += '0' # 소수점에 0 추가해주고
        # N은 그대로        
        
        # 계산이 되었든 안 되었든 다음 소수점 확인해야 함
        x += 1 # 따라서 소수점 idx +1     

        if x == 13: #13자리 이상이라면 
            decimal = 'overflow'
            break    

    print(f"#{tc} {decimal}")
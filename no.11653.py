"""
Q)
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

I)
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

O)
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
"""

N = int(input())
if N == 1:
    print('')

for i in range(2, N+1): # 아래 코드와 달리 for문 한번으로 해결
    if N % i == 0:
        # N을 i로 나눌 수 없을 때까지 나누기
        while N % i == 0:
            print(i)
            N = N // i
    elif N == 1: break # N이 더이상 나눠지지 않음 근데 이거 추가했더니 더 시간 오래걸림,,

"""  반복문이 너무 많음. for 문을 n-1번 반복해야함, 시간 초과!          
while num != N-1:
    for i in range(2,N):
        if N % i == 0:  # i 가 N의 소인수
            f_list.append(i)
            N = int(N / i)  # N을 i로 나누고 다시 for 루트 시작
            break
        else:
            num = num+1  #N이 소수일때 num 은 루트를 돈 횟수
f_list.append(N) # 마지막으로 남은 N(소수) 추가

for x in f_list: print(x)
"""

"""
Q)
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

I)
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

O)
첫째 줄에 N!을 출력한다.

풀이) 재귀 함수를 이용하여 팩토리얼 구하기

풀이2) for문 사용
result = 1
if n>0:
    for i in range(1, n+1):
        result = result*i
print(result)

# 0! = 1 인 이유

1! = 1 * (1-1)!
   = 1 * 0! = 1
따라서 0! = 1
"""
def fac(num):
    result = 1 # 0! = 1
    if num>0:
        result = num * fac(num-1) # 재귀 함수(자기자신을 호출하는 함수)
    return result
N = int(input())
print(fac(N))
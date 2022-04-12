"""
Q)
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

I)
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

O)
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""

"""처음 풀이 - 시간초과
m, n = map(int, input().split())
for i in range(m, n+1):
    primeNum = True
    if i ==1:
        primeNum = False
    else:
        for k in range(2, i):
            if i % k == 0:
                primeNum = False
                break
    if primeNum :
        print(i)
        # elif i == 3 or i ==2:
        #     print(i)
"""           

#에라토스테네스의 체를 이용하여 시간 단축 -> ex) 6 = 2 * 3 = 3 * 2 로 대칭
# 에라토슽네스의 체 : 특정한 숫자의 제곱근까지만 약수의 여부를 검증. 시간복잡도: O(n^(1/2))
#                    일반적인 소수 판별 알고리즘의 시간복잡도: O(n)


def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):  # 제곱근까지만 검증
            if num % n == 0: # 소수가 아님
                return False
        
        return True # 소수

m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)
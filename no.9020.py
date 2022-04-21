"""
Q)
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 
하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

I)
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

O)
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
4 ≤ n ≤ 10,000

풀이 1) 시간초과
먼저 10000 까지 모든 소수 찾기
이중 for 문(n보다 작은 값) 이용하여 만족하는 a와 b 찾고 a - b 값을 다른 리스트에 추가
답이 한 개 이면 바로 출력
아니면 차를 구한 리스트를 절대값으로 정렬 후 가장 먼저 값 출력
 
풀이 2) 시간초과 개빡침
먼저 10000 까지 모든 소수 찾기
a 찾고 n-a가 소수인지 판별

풀이 3) 최솟값을 찾는 것에서 힌트!!! 이중 for문 없애기
n/2 에서 부터 n/2-1, n/2+1 에서부터 찾아보기

"""

def isPrime(num): # 소수 판별 함수
    if num == 1:
        return False
    else:
        for x in range(2, int(num**0.5)+1): # 에라토스테네스의 체
            if num % x == 0:
                return False
        return True

def goldP(n): 
    for num in range(n//2+1):
        if n//2-num in prime_list and n//2+num in prime_list:
            print(str(int(n//2-num))+" "+str(int(n//2+num)))   
            break

all_list = [x for x in range(10000)]
prime_list = [] # 범위 내의 모든 소수

for i in all_list:
    if isPrime(i):
        prime_list.append(i)

T = int(input())
for t in range(T):
    n = int(input())
    goldP(n)

"""
all_list = [x for x in range(10000)]
prime_list = [] # 범위 내의 모든 소수

def goldP(n):
    for a in range(2, n/2 + 1): # 중복 안나오게
        if a in prime_list and n-a in prime_list:
            if not anw: # anw 비었을때
                anw.append(a) # a
                anw.append(n-a) # b
            else:
                if anw[1] - anw[0] > n - 2*a:
                    anw[0] = a
                    anw[1] = n-a
    return anw
for i in all_list:
    if isPrime(i):
        prime_list.append(i)
for t in range(T):
    n = int(input())
    anw = []
    anw2 = [] # a b의 차를 담을 리스트
    for i in range(len(prime_list)):
        if prime_list[i] > n:
            break
    for a in prime_list[:i]:
        for b in prime_list[:i]:
            if a+b == n:
                anw.append([a,b])
                k = a - b
                anw2.append(k)
    # print(anw)
    if len(anw) == 1: # 답이 한 개 == a 와 b 가 같음.
        print("%d %d"%(anw[0][0],[0][1]))           
    
    else: # 답이 여러 개        
        # print(anw2)
        new_anw2 = sorted(anw2, key = abs) # 절대값 기준으로 정렬
        min_list = anw[anw2.index(new_anw2[0])] 
        print("%d %d"%(min_list[0],min_list[1]))
"""

"""
for t in range(T):
    n = int(input())
    # a는 2부터 n/2 까지의 수 중 소수인 수(작은 수 부터 출력해야 함)
    # b는 n - a 이며 소수인 수
    for i in range(len(prime_list)):
        if prime_list[i] >= n/2:
            break
    anw = []
    anw2 = []
    for a in prime_list[:i+1]:
        if n-a in prime_list:
            anw.append([a, n-a])
            anw2.append(2*a - n)
    
    if len(anw) == 1: # 답이 한 개 == a 와 b 가 같음.
        print("%d %d"%(anw[0][0],[0][1]))           
    
    else: # 답이 여러 개        
        # print(anw2)
        new_anw2 = sorted(anw2, key = abs) # 절대값 기준으로 정렬
        min_list = anw[anw2.index(new_anw2[0])] 
        print("%d %d"%(min_list[0],min_list[1]))
"""


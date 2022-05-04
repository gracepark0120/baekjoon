"""
Q)
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

I)
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

O)
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

https://www.daleseo.com/sort-bubble/ # 버블 정렬

"""

N = int(input())
n_list = []
for _ in range(N):
    n = int(input())
    n_list.append(n)

n_set = set(n_list)
n_list = list(n_set)
n_list.sort()

for i in n_list:
    print(i)

# 버블 정렬
n = int(input())

m= []

for i in range(n):
    m.append(int(input()))
def bubble_sort(arr):
    end = len(arr)-1
    while end > 0:
    #for i in range(len(m)-1, 0, -1): # 외부 반복문 : 정렬범위를 n-1 부터 1 까지 줄여감
        last_swap = 0
        swapped = False
        for j in range(i):
            if m[j] > m[j+1] : 
                m[j], m[j+1] = m[j+1], m[j]
                swapped = True
        if not swapped:
            break
# 삽입 정렬

n = int(input())

m= []

for i in range(n):
    m.append(int(input()))

for k in range(1, len(m)): # key
    for i in range(0,len(m)-1):
        if m[k] < m[i] :
            m[k], m[i] = m[i], m[k]
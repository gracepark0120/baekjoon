"""
Q)
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

in)
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

out)
주어진 수들 중 소수의 개수를 출력한다
"""

n = int(input())
list = list(map(int, input().split()))
anw = 0

for i in list:
    if i == 1  : continue
    num = 2
    while num < i:
        if i % num ==0:  break# 합성수
        else : num += 1
    if num == i: # while문에서 break 없이 끝남
        anw += 1

print(anw)


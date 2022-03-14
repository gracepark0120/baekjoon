"""
Q)
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다.
또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

in)
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

out)
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

"""

""" 처음 코드 -> 부등식 계산 때문에 시간초과.
a, b, v = map(int, input().split())
n = 1  # 걸릴 날짜
sum = 0

while sum < v :
    sum = sum + a
    if sum >= v:
        break
    else :
        sum = sum - b
        n += 1

print(n)
"""
# an - b(n-1) >= v   <=> n = (v-b)//(a-b) +1
a, b, v = map(int, input().split())
n = (v-b)/(a-b)
print(int(n) if n == int(n) else int(n) + 1)
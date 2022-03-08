"""
Q)
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

in)
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

out)
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

#내 풀이 : 하나씩 비교했는데, 리스트 내의 최댓값을 알려주는 max라는 매소드가 존재했음.
(min도 존재)
list = []
for _ in range(9):
    list.append(int(input()))

max_num = list[0]
max_id = 0
for i in range(9):
    if list[i] > max_num:
        max_num = list[i]
        max_id = i+1
"""

num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)


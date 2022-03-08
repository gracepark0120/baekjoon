"""
Q) 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
ex)
1-99 모두 한수
100-999 는 비교해봐야함

in)
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

out)
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

"""

N = int(input())
num = 99

if N<100:
    print(N)
else:
    for i in range(100, N+1):
        n_list = list(map(int, str(i)))
        if n_list[0] == n_list[1] == n_list[2]:
            num += 1
        elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            num += 1
    print(num)

"""
Q)
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
in)
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

out)
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

한번에 출력
test_list = []
out_list=[]
n = int(input())
for i in range(n):
    test_list.insert(i, list(map(int, input().split())))
    num = 0
    avg = sum(test_list[i][1:]) / test_list[i][0]
    for a in test_list[i][1:]:
        if a > avg:
            num = num +1
    out_list.insert(i, round(num/test_list[i][0]*100, 3))
"""
#한줄 입력 한줄 출력
n = int(input())
print()
for _ in range(n):
    test_list = list(map(int, input().split()))
    avg = sum(test_list[1:])/test_list[0]
    num = 0
    for i in test_list[1:]:
        if i>avg:
            num = num +1
    print(f'{num/test_list[0]*100:.3f}%')
  #  print(round(num/test_list[0] * 100,3), "%", sep = "")
  #  이게 틀린 이유: 소수 셋째자리 까지 출력해야하는데 round 사용시 반올림만 해주므로
  #  만약 주어진 숫자가 소수 셋째자리까지 없다면 셋째자리까지 출력 안됨.

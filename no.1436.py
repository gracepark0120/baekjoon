"""
Q)
1시간 고민 - 안됨.. 
666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 
영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 
조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 
피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.

하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.

종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 
제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.

따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 
숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

I)
첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

O)
첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.

666 1666 2666 3666 4666 5666 6660 6661 6662 6663 
6664 6665 6666 6667 6668 6669 7666 8666 9666 10666 
11666 12666 13666 14666 15666 16660 16661 16662 16663 16664
16665 16666 16667 16668 16669 17666 18666 19666 20666 21666
22666 23666 24666 25666 26660

풀이 1) 실패
N을 받아서 분해하여 생각한 규칙에 따라 답을 구하여 출력
-> 규칙을 찾을 수 가 없음, 실패
def find_n(N):
    if N <= 6:
        return str(N-1)+"666"
    else:
        a = (N-6)%19 # 나머지
        b = (N-6)//19 # 몫
        n = N-6
        if a==0:
            return str(15+10*(b-1))+"666" #
        elif a < 11:
            return str(b)+"666"+str(a-1)
        else :
            return str(b*10+a-4)+"666"


풀이 2) 발상의 전환
숫자를 계속 증가시켜서 666이 들어가면 cnt를 1 추가.
cnt 가 n 이 되면 증가시킨 숫자 출력 

-> 시간이 오래 걸릴 것이라 생각해 풀이 1을 생각했었지만.. 이게 낫다.
"""
N = int(input())
    
cnt = 0
six_n = 666

while True:
    if '666' in str(six_n):
        cnt = cnt +1
    if cnt == N:
        print(six_n)
        break
    six_n += 1
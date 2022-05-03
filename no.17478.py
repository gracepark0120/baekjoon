"""
Q)
평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.
매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.
중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.
떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.

I)
교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

O)
출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.
"""
""" return을 사용한 재귀함수 사용법
arr = [
        '"재귀함수가 뭔가요?"\n',
        '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n',
        '라고 답변하였지.\n'
]       

def reply(N,a):

    under_bar = "____"
    
    if N==0: # 마지막 라인 
        re = under_bar*a+arr[0]+under_bar*a+'"재귀함수는 자기 자신을 호출하는 함수라네"\n'+under_bar*a+arr[4]
        
    else:
        nre_1 = under_bar*(a-N) + arr[0]
        nre_2 = under_bar*(a-N) + arr[1]
        nre_3 = under_bar*(a-N) + arr[2]
        nre_4 = under_bar*(a-N) + arr[3]
        nre_5 = under_bar*(a-N) + arr[4]
        re = nre_1 + nre_2 + nre_3 +nre_4+reply(N-1,a)+nre_5
        
    return re
N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
a=N # N을 a에 보관
print(reply(N,a))
       
"""

# return 을 사용하지 않은 재귀함수
# return 은 함수 중간에서 바로 빠져나오는 기능도 있음.
arr = [
        '"재귀함수가 뭔가요?"',
        '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',
        '라고 답변하였지.'
] 

def reply_2(N, cnt):
    # 카운트 수가 증가할 때 마다 under_bar 추가
    under_bar = "____"

    if N == cnt:
        print(under_bar + arr[0])
        print(under_bar + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(under_bar + arr[4])
        return # 함수 빠져나옴. 
    
    for i in arr[:4]:
        print(under_bar+ i)
    cnt = cnt + 1

    reply_2(N, cnt)
    print(under_bar + arr[4])

N = int(input())
print("어느 한 ...")
reply_2(N, cnt)
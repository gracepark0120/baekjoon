"""
Q)  두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
input)
 입력은 여러 개의 테스트 케이스로 이루어져 있다.
 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

output)
 각 테스트 케이스마다 A+B를 출력한다.

 eof : end of file 파일 입출력 시 입력이 끝날때까지 읽어들임
 EOFError : 입력 도중에 파일의 끝을 만나면 EOFError가 발생
 while문 사용시 종결규칙이 없음 출력이 완료되고 아무것도 입력 안했을 때 빠져나와야 하므로
 except에 eoferror를 적어 error 가 났을 때 break 하게 구현.
"""

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

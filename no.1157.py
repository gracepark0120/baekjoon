"""
Q)
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

in)
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

out)
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

"""
from string import ascii_lowercase
from string import ascii_uppercase

a = input()
#입력받은 단어 리스트로
a_list = list(map(str, a))
alpha_list = list(ascii_lowercase)
alpha_uplist = list(ascii_uppercase)

#입력받은 단어에 사용된 알파벳 수 저장할 리스트
num_list = []

for a in alpha_list:
    #소문자 리스트에 있는 알파벳 대문자로 바꿈
    b = chr(ord(a) - 32)
    #소문자/대문자 수 각각 세서 num_list에저장
    num = a_list.count(a) + a_list.count(b)
    num_list.insert(alpha_list.index(a), num)

#가장 많은 알파벳 수
max_num = max(num_list)

#가장 많이 사용된 알파벳 여러개 일 때
if num_list.count(max_num) > 1:
    print("?")

else :
    print(alpha_uplist[num_list.index(max_num)])
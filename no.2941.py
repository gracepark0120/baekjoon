"""
Q)
크로아티아 알파벳	변경
č	c=
ć	c-
dž	dz=
đ	d-
lj	lj
nj	nj
š	s=
ž	z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

in)
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

out)
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

정석 풀이:
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, '*')
print(len(word))
"""

sentence = input()
sen_list = list(map(str, sentence))
num = 0
# for a in sen_list: 로 하면 같은 문자 (= 이나 -) 나올때 index찾기 힘듦, 길이로 for 문 돌리기
length = len(sen_list)

for a in range(length):
    if sen_list[a]== '=' :
        if sen_list[a-2] == 'd' and sen_list[a-1] == 'z' :
            num = num-1
        elif sen_list[a-1] == 'c' or sen_list[a-1] == 's' or sen_list[a-1] == 'z':
           num +=0
        else:
            num += 1

    elif sen_list[a]== '-':
        if sen_list[a-1] == 'c' or sen_list[a-1] == 'd':
            num += 0
        else :
            num +=1

    elif sen_list[a]=='j':
        if sen_list[a-1] == 'l' or sen_list[a-1] == 'n' :
            num += 0
        else :
            num += 1

    else :
        num += 1

print(num)


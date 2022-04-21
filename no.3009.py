"""
Q)세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

I)세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

O)직사각형의 네 번째 점의 좌표를 출력한다.

"""
x,y = map(int, input().split()) # (x, y) 좌표
w,z = map(int, input().split()) # (w, w) 좌표
a,b = map(int, input().split()) # (a, b) 좌표

# (m, n) 좌표 구하기
if x == w: 
    m = a # 가로
    if b == y:
        n = z # 세로
    elif b == z:
        n = y
elif w == a:
    m = x
    if y == z:
        n = b
    elif y == b:
        n = z
elif x == a:
    m = w
    if z == y:
        n = b
    elif z == b:
        n = y

print(str(m)+" "+str(n))
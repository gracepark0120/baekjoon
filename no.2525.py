
h,m = map(int, input().split())
a= int(input())

m = a+m
while m >= 60:
    h = h+1
    m = m-60
    if h >= 24:
        h = h - 24
print(h, m)

import sys
for i in sys.stdin:
    sd = int(i)
    fd = 1
    x = 1
    n=0
    for i in range(50):
        n += x
        x += fd
        fd += sd
    print(n)
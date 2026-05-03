A, B = input().split()
#'10 20' -> ['10','20']
A, B = int(A), int(B)
#10 20
if A > B:
    print(A)
else:
    print(B+1)
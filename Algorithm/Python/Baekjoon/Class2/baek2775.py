import sys

T = int(sys.stdin.readline())
for t in range(T):
    num = 0
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    r_list = list(range(1, room+1))
    a_list = [r_list]
    for f in range(floor):
        for r in range(len(r_list)):
            if r == 0:
                continue
            else:
                r_list[r] = r_list[r]+r_list[r-1]
    print(r_list[-1])
    
    
        
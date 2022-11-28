prev = 0
curr = 1
nex = 2

while curr < 100:
    print(curr)
    prev = curr
    curr = nex
    nex = prev + curr
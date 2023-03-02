import math
import os
def fun(x):
    return math.tan(x)
def test(start,end):
    mid = (start + end) / 2
    count = 0
    while (abs(mid - math.pi) > 0.000000005):
        if fun(start)*fun(mid) < 0:
            end = mid
            #print("f({}) * f({}) < 0".format(start,end))
            #print(end)
            mid = (start + end) / 2
        elif fun(end)*fun(mid) < 0:
            start = mid
            #print("f({}) * f({}) < 0".format(start,end))
            #print(start)
            mid = (start + end) / 2
        count += 1
    print(count)
test(2,7)
os.system("pause")

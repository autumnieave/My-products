import math
import os
def fun(x):
    return math.exp(x)-2-x
def test(start,end):
    f_head = fun(start)
    f_end = fun(end)
    print("Head:{}".format(f_head))
    count = 0
    while f_head*f_end < 0:
        count += 1
        d_x = end - start
        d_y = (f_end - f_head)
        k = d_y/d_x
        b = f_end - k*end
        end = -b/k
        f_end = fun(end)
        print("end_{}:{}".format(count-1,f_end))
        print("k:{}".format(k))
        print("x:{}".format(-b/k))
test(-2.4,-1.6)
os.system("pause")

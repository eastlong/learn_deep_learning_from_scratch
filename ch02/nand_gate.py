"""
NAND是Not AND，与非门就是颠倒了与门的输出。
仅当x1和x2同时为1时输出0，其他时候则输出1。
"""
import numpy as np

"""
与非门
"""
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 仅仅权重和偏置与 AND 不同
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

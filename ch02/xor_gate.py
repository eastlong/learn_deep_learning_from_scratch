from and_gate import AND2
from or_gate import OR
from nand_gate import NAND

"""
异或门
仅当x1或x2中的一方为1时，才会输出1（“异或”是拒绝其他的意思）。
"""
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND2(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))  
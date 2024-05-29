class Solution:
    def numSteps(self, s: str) -> int:
        c = int(s, 2)
        c2 = 0
        while c != 1:
            c2 += 1
            if c % 2 == 1:
                c += 1
            else:
                c //= 2
        return c2

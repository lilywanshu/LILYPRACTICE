def reverse(self, x: int) -> int:
    fac_2 = 2 ** 31
    mul = -1 if x < 0 else 1
    x2 = list(str(abs(x)))
    opposite = [''] * len(x2)
    for i in range(len(x2)):
        opposite[len(x2)-1-i] = (x2)[i]
    result = int(''.join(opposite)) * mul
    if result < -fac_2 or result > fac_2 - 1:
        return 0
    return result

print(reverse(None, -(2 ** 31)))
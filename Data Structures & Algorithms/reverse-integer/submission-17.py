class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        print(str_x)
        res = 0
        mult = 1
        if x < 0:
            mult = -1
            res = int("-" + str(res))
            str_x = str_x[1:]
        MAX = pow(2, 31) - 1
        MIN = -1 * pow(2, 31)
        print(MAX)
        print(MIN)
        for ch in reversed(str_x):
            if res > MAX // 10:
                return 0
            elif res < MIN // 10:
                return 0
            elif res == MAX // 10 and int(ch) > MAX % 10:
                return 0
            elif res == MIN // 10 and int(ch) > MIN % 10:
                return 0
            res = int(str(res) + ch)
            print(res)
        return res * mult
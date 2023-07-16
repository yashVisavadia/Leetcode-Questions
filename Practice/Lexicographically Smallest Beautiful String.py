class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        def check(i):
            return (i > 0 and s[i] == s[i - 1]) or (i > 1 and s[i] == s[i-2])

        s = [ord(ch) - ord('a') for ch in s]
        s[-1] += 1
        i = 0
        while i < len(s):
            if s[i] >= k:
                s[i] = 0
                i -= 1
                if i > -1:
                    s[i] += 1
                else:
                    break
            elif check(i):
                s[i] += 1
            else:
                i += 1

        if i == -1:
            return ''

        return ''.join([chr(ord('a') + num) for num in s])

        # def check(i):
        #     return (i > 0 and s[i] == s[i - 1]) or (i > 1 and s[i] == s[i - 2])

        # s = [ord(c) - ord("a") for c in s]
        # s[-1] += 1
        # i = len(s) - 1

        # while i >= 0 and i < len(s):
        #     if s[i] >= k:
        #         s[i] = 0
        #         i -= 1
        #         if i > -1:
        #             s[i] += 1
        #         else:
        #             break
        #     elif check(i):
        #         s[i] += 1
        #     else:
        #         i += 1

        # if i == -1:
        #     return ""

        # ans = []
        # for num in s:
        #     ans.append(chr(ord("a") + num))

        # return "".join(ans)


obj = Solution()
s = "abcz"
k = 26
print(obj.smallestBeautifulString(s, k))

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = 0
        res = ''

        for ch in s:
            if ch.isnumeric():
                num = num * 10 + int(ch)
            elif ch == '[':
                st.append(res)
                st.append(num)
                res = ''
                num = 0
            elif ch == ']':
                cnt = st.pop()
                prev = st.pop()
                res = prev + cnt * res
            else:
                res += ch
        return res


obj = Solution()
s = "3[a2[c]]"
print(obj.decodeString(s))

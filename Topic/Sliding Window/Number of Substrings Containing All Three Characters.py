class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = [0] * 3
        j = 0
        ans = 0

        while j < len(s):
            cnt[ord(s[j]) - ord('a')] += 1
            if all(cnt):
                st = j
                cnt_2 = [0] * 3
                while not all(cnt_2):
                    cnt_2[ord(s[st]) - ord('a')] += 1
                    st -= 1
                ans += st + 2
            j += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = 'abababccc'
    print(sol.numberOfSubstrings(s))

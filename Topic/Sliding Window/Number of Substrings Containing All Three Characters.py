class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        ind_a = ind_b = ind_c = -1
        ans = 0

        for i in range(len(s)):
            if s[i] == 'a':
                ind_a = i
            elif s[i] == 'b':
                ind_b = i
            else:
                ind_c = i
            ans += min(ind_a, ind_b, ind_c) + 1
        return ans

        # cnt = [0] * 3
        # j = 0
        # ans = 0

        # while j < len(s):
        #     cnt[ord(s[j]) - ord('a')] += 1
        #     if all(cnt):
        #         st = j
        #         cnt_2 = [0] * 3
        #         while not all(cnt_2):
        #             cnt_2[ord(s[st]) - ord('a')] += 1
        #             st -= 1
        #         ans += st + 2
        #     j += 1
        # return ans


if __name__ == "__main__":
    sol = Solution()
    s = 'abababccc'
    print(sol.numberOfSubstrings(s))

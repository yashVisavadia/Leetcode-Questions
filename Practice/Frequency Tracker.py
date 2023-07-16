from collections import Counter, defaultdict


class FrequencyTracker(object):
    def __init__(self) -> None:
        self.f = Counter()
        self.g = Counter()

    def add(self, number):
        self.f[number] += 1
        self.g[self.f[number]] += 1
        self.g[self.f[number] - 1] -= 1

    def deleteOne(self, number):
        if self.f[number]:
            self.f[number] -= 1
            if self.f[number] == 0:
                del self.f[number]
            self.g[self.f[number]] += 1
            self.g[self.f[number] + 1] -= 1

    def hasFrequency(self, frequency):
        return self.g[frequency] > 0

    # def __init__(self):
    #     self.f, self.g = defaultdict(int), defaultdict(int)

    # def add(self, number):
    #     """
    #     :type number: int
    #     :rtype: None
    #     """
    #     # self.f[number], self.g[self.f[number] - 1], self.g[self.f[number]] = self.f[number] + 1, self.g[self.f[
    #     #     number]] - 1 if self.f[number] else self.g[self.f[number]], self.g[self.f[number] + 1] + 1

    # def deleteOne(self, number):
    #     """
    #     :type number: int
    #     :rtype: None
    #     """
    #     if self.f[number] > 0:
    #         self.f[number], self.g[self.f[number] + 1], self.g[self.f[number]] = self.f[number] - 1, self.g[
    #             self.f[number]] - 1, self.g[self.f[number] - 1] + 1

    # def hasFrequency(self, frequency):
    #     """
    #     :type frequency: int
    #     :rtype: bool
    #     """
    #     return self.g[frequency] > 0

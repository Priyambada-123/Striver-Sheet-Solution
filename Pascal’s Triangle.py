class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(numRows):
            a.append([1] * (i + 1))
            for j in range(1, len(a[i]) - 1):
                a[i][j] = a[i-1][j-1] + a[i-1][j]

        return a
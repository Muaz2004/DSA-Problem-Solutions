class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevRow = self.getRow(rowIndex - 1)
        currRow = [1 for _ in range(len(prevRow) + 1)]

        for i in range(1, len(currRow) - 1):
            currRow[i] = prevRow[i] + prevRow[i - 1]
        
        return currRow
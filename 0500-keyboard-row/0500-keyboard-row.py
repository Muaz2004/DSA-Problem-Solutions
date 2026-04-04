class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        result=[]
        for i in words:
            for ch in i:
                if ch.lower() not in row1:
                    break
            else:
                result.append(i)
            for ch in i:
                if ch.lower() not in row2:
                    break
            else:
                result.append(i)
            for ch in i:
                if ch.lower() not in row3:
                    break
            else:
                result.append(i)
        return result
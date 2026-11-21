class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl,rr=0,len(matrix)-1
        row=0
        while rl<=rr:
            m=(rl+rr)//2
            if matrix[m][0]==target:
                return True
            if rl==rr:
                row=m
                break
            if matrix[m][0]<target and matrix[m+1][0]>target:
                row=m
                break
            elif matrix[m][0]>target:
                rr=m-1
            else:
                rl=m+1
        l,r=0,len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
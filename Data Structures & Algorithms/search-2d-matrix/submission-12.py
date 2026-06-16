class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def traverseRow(row):
        #     answer = False
        #     for j in range(len(matrix[0])):
        #         if matrix[row][j] == target:
        #             answer = True
        #     return answer
        # # look at the first entry of every row first and if the entry 
        # # is lower than target, go to previous row and look through
        # answer = False
        # for i in range(len(matrix)):
        #     if i == len(matrix) - 1:
        #         print("Last Row")
        #         answer = traverseRow(i)
        #         break
        #     if matrix[i][0] < target:
        #         print("Less")
        #         continue
        #     if matrix[i][0] == target:
        #         return True
        #     if matrix[i][0] > target:
        #         print("More")
        #         i = i - 1
        #         answer = traverseRow(i)
        #         break
        # return answer

        # Binary search algorithm
        def binarySearch(row, start, end):
            while start <= end:
                mid = (end-start) // 2 + start
                print("Mid: ", matrix[row][mid])
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        row  = 0
        col_max = len(matrix[0]) - 1
        while row < len(matrix):
            if matrix[row][0] <= target and matrix[row][col_max] >= target:
                return binarySearch(row, 0, col_max)
            else:
                row += 1
        
        return False
 
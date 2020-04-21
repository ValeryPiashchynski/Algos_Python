class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        cur_r = 0
        cur_c = cols - 1

        while cur_r < rows and cur_c >= 0:
            if binaryMatrix.get(cur_r, cur_c) == 0:
                cur_r += 1
            else:
                cur_c -= 1

        return cur_c + 1 if cur_c != cols - 1 else -1
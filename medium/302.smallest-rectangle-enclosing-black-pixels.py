# You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.
#
# The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.
#
# Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
#
# You must write an algorithm with less than O(mn) runtime complexity
#
#
#
# Example 1:
#
#
#
# Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
# Output: 6
# Example 2:
#
# Input: image = [["1"]], x = 0, y = 0
# Output: 1
#
#
# Constraints:
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 100
# image[i][j] is either '0' or '1'.
# 0 <= x < m
# 0 <= y < n
# image[x][y] == '1'.
# The black pixels in the image only form one component.
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # 03/27/2024
        # for rows and cols separatly, find the first and last occurance of 1
        # note we can use x/y as boundary instead of 0-end
        # to check if a row or col has 1 is O(n)
        def checkRow(r):
            return 1 in image[r]

        def checkCol(c):
            for i in range(len(image)):
                if image[i][c]:
                    return True
            return False

        # first of col(left bound of black pixel)
        s, e = 0, y
        while s < e:
            mid = (s + e) // 2
            if checkCol(mid):
                # col mid has 1, self or go left
                e = mid
            else:
                s = mid + 1
        left = s
        # last of col(right bound of black pixel)
        s, e = y, len(image[0]) - 1
        while s + 1 < e:
            mid = (s + e) // 2
            if checkCol(mid):
                # col mid has 1, self or go right
                s = mid
            else:
                e = mid - 1
        right = e if checkCol(e) else s

        # first of row(up bound of black pixel)
        s, e = 0, x
        while s < e:
            mid = (s + e) // 2
            if checkRow(mid):
                # row mid has 1, self or go up
                e = mid
            else:
                s = mid + 1
        up = s
        # last of row(down bound of black pixel)
        s, e = x, len(image) - 1
        while s + 1 < e:
            mid = (s + e) // 2
            if checkRow(mid):
                # row mid has 1, self or go down
                s = mid
            else:
                e = mid - 1
        down = e if checkCol(e) else s

        return (up - down + 1) * (right - left + 1)

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # 03/27/2024
        # similar to previous solution
        # to get right bound, we need to get the first 0 starting from x/y
        # pass in the function to check row or check col, use lambda to control
        # direction
        left = self.search(image, 0, y, self.checCol)
        up = self.search(image, 0, x, self.checRow)
        right = self.search(
            image, y + 1, len(image[0]) - 1, lambda col: not self.checCol(col)
        )
        down = self.search(
            image, x + 1, len(image) - 1, lambda row: not self.checRow(row)
        )
        return (right - left) * (down - up)

    def search(self, image, s, e, check: callable):
        # find first occurance
        # for left and up, find first occurance of 1
        # for right and down, find first occurance of 0
        while s < e:
            mid = (s + e) // 2
            if check(mid):
                # find occurance
                e = mid
            else:
                s = mid + 1
        return s

    def checRow(self, image, row):
        return 1 in image[row]

    def checCol(self, image, col):
        for i in range(len(image)):
            if image[i][col]:
                return True
        return False

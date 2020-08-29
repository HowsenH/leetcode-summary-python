""" Min Cost to Racing Track end


There are three racing tracks. The car departs from middle of the racing track. 
There are obstacles on the racing track. Given a int array to indicate which 
racing track have obstacles. Ask at least a few turn cost to end of racing track.


Author: Weikun Han <weikunhan@g.ucla.edu>

Reference: https://www.1point3acres.com/bbs/thread-642190-1-1.html

Time complexity:  O(n)
Space complexity: O(1)

Example 1:
Input: 
obstacles = [0, 1]
Output: 
1 
Explanation: 
Start from line 1. The first obstacle in line 0 and not change line 
The second obstacle in line 1 and need to change 1 (cost add 1). Total cost is 1

Example 2:
Input: 
obstacles = [1, 2, 0, 1]
Output: 
3
Explanation:
Start from line 1. The first obstacle in line 1 and need to change line (cost add 1)
The second obstacle in line 2, if you last change to line 2 which need change line 
(cost add 1) and if you last change to line 0 which no need change line.
The Third obstacle in line 0, if you last change to line 0 which need change line 
(cost add 1) and if you last change to line 2.
The fourth obstacle in line 1, if you stay in last line 0 or line 2, you don't
need to change line. Total cost is 3

Example 3:
Input:
obstacles = [0, 1, 1, 2, 1, 2, 1, 1, 0]
Output: 
2
Explanation:
Change line 1 to line 0 and change back to line 1. Total cost is 2.

Example 4:
Input:
obstacles = [1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 2, 1]
Output: 
3
Explanation:
Change to line 2 then change to 0.
"""

class Solution(object):
    def min_cost_to_racing_track_end(self, obstacles):
        """
        :type nums: List[int]
        :rtype: int
        """

        value_list = [1, 0, 1]
        
        for i in obstacles:
            a, b, c = value_list
            if i == 0:
                value_list = [min(a+2, b+1), b, c]
            if i == 1:
                value_list = [a, min(a+1, b+2, c+1), c]
            if i == 2:
                value_list = [a, b, min(b+1, c+2)]
        
        return min(value_list)

def main(): 
    obstacles = [0, 1, 1, 2, 1, 2, 1, 1, 0]
    solution = Solution()
    res = solution.min_cost_to_racing_track_end(obstacles)
    print(res)

if __name__ == "__main__": 
    main()
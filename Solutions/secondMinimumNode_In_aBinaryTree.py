# Q2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = [root.val]
        second_min = [float('inf')]

        def dfs(node):
            if not node:
                return

            if min_val[0] < node.val < second_min[0]:
                second_min[0] = node.val
            elif node.val == min_val[0]:
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        if second_min[0] != float('inf'):
            return second_min[0]
        else:
            return -1

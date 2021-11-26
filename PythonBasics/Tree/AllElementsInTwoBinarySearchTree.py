# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []
        list = []
        if root1 or root2:
            list += [root1.val] + self.getAllElements(root1.left, root2.left) + self.getAllElements(root1.right,
                                                                                                    root2.right)
            print(list.sort())

        return list.sort()



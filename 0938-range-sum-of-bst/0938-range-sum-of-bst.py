class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inOrderTraversal(node):
            nonlocal temp
            if not node:
                return
            if low <= node.val <= high:
                temp += node.val
            if node.val > low:
                inOrderTraversal(node.left)
            if node.val < high:
                inOrderTraversal(node.right)

        temp = 0
        inOrderTraversal(root)
        return temp
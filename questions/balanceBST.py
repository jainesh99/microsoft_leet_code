class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorderTraverse(node, nodeList):
            if node:
                inorderTraverse(node.left, nodeList)
                nodeList.append(node)
                inorderTraverse(node.right, nodeList)

        def buildBST(nodeList, left, right):

            if left > right:
                return None
            mid = (left + right) // 2
            node = nodeList[mid]
            node.left = buildBST(nodeList, left, mid - 1)
            node.right = buildBST(nodeList, mid + 1, right)
            return node

        nodeList = []
        inorderTraverse(root, nodeList)
        root = buildBST(nodeList, 0, len(nodeList) - 1)
        return root
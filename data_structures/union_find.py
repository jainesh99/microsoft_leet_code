class UnionFind:
    def __init__(self, N):
        self.ufid = [i for i in range(N + 1)]

    def find(self, node):
        root = node
        while root != self.ufid[root]:
            root = self.ufid[root]

        # path compresssion
        p = node
        while p != root:
            parent = self.ufid[p]
            self.ufid[p] = root
            p = parent

        return root

    def union(self, x, y):
        root1, root2 = self.find(x), self.find(y)

        if root1 == root2:
            return False

        self.ufid[root1] = root2

        return True

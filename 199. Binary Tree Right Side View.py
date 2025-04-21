class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        from collections import deque
        que = deque([root])
        vw = []
        
        while que:
            lvl = len(que)
            for i in range(lvl):
                node = que.popleft()
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
                if i == lvl - 1:
                    vw.append(node.val)
        
        return vw
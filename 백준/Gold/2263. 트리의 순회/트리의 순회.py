# 2263 트리순회
import sys
sys.setrecursionlimit(10**6)

def preorder(inorder_s, inorder_e, postorder_s, postorder_e):
    # 기저 조건
    if inorder_s > inorder_e:
        return

    root = postorder[postorder_e]
    root_idx = val_dict[root]

    left_ln = root_idx - inorder_s

    # root 노드 출력
    print(root, end=' ')
    # 왼쪽 서브트리
    preorder( inorder_s, root_idx-1, postorder_s, postorder_s+left_ln-1)
    # 오른쪽 서브트리
    preorder( root_idx+1, inorder_e, postorder_s + left_ln, postorder_e-1)


n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
val_dict = {}

for idx, value in enumerate(inorder):
    val_dict[value] = idx


preorder(0, n-1, 0, n-1)
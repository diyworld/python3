# 节点
tnodeA = {'idx':0, 'right':-1, 'child':1, 'data':'A'}
tnodeB = {'idx':1, 'right':2, 'child':4, 'data':'B'}
tnodeC = {'idx':2, 'right':3, 'child':7, 'data':'C'}
tnodeD = {'idx':3, 'right':-1, 'child':-1, 'data':'D'}

tnodeE = {'idx':4, 'right':5, 'child':-1, 'data':'E'}
tnodeF = {'idx':5, 'right':6, 'child':-1, 'data':'F'}
tnodeG = {'idx':6, 'right':-1, 'child':-1, 'data':'G'}
tnodeH = {'idx':7, 'right':-1, 'child':-1, 'data':'H'}

tnodeI = {'idx':8, 'right':9, 'child':-1, 'data':'I'}
tnodeJ = {'idx':9, 'right':-1, 'child':-1, 'data':'J'}

# 节点列表
treelist = [tnodeA, tnodeB, tnodeC, tnodeD, tnodeE, tnodeF, tnodeG, tnodeH, tnodeI, tnodeJ]
# 遍历树
def travtree(tlist, idx):
    i = tlist[idx]['idx']
    c = tlist[idx]['child']
    r = tlist[idx]['right']
    if i >= 0:
        print(tlist[i]['data'], end=' ')
    if c > 0:
        travtree(tlist, c)
    if r > 0:
        travtree(tlist, r)

# 新增节点
def addnode(tlist, node, parentidx):
    tlist.append(node)
    node['idx'] = len(tlist) - 1
    node['child'] = -1
    node['right'] = -1
    node['data'] = chr(ord('A') + node['idx'])
    idx = tlist[parentidx]['child']
    if parentidx < 0:
        return
    if idx < 0:
        tlist[parentidx]['child'] = node['idx']
        return
    right = idx
    while right >= 0:
        idx = right
        right = tlist[right]['right']
    tlist[idx]['right'] = node['idx']
    
travtree(treelist, 0)
print()

testlist = []
addnode(testlist, tnodeA, -1)
addnode(testlist, tnodeB, 0)
addnode(testlist, tnodeC, 0)
addnode(testlist, tnodeD, 0)
travtree(testlist, 0)
print()








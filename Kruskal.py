n = 7
graph = [[1,2,1], [1,3,4], [2,3,7], [2,4,3], [2,6,10], [3,5,5], [3,6,4], [4,6,6], [4,7,9], [5,6,2], [6,7,8]]
# n: 총 노드의 수
# graph: 그래프 내의 간선 정보들 - [노드A, 노드B, 비용]

p = [0]

# 해당 노드의 루트 노드(최상위 노드)를 return
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
        
    return p[x]

# 2개의 트리를 하나로 결합하고 루트 노드도 하나로 변경
def union(x, y):
    root1 = find(x)
    root2 = find(y)
    p[root2] = root1


mst = []
# mst: 최소 신장 트리

# 간선 정보들을 비용이 가장 낮은 것부터 정렬
graph.sort(key = lambda x: x[2])

for i in range(1, n+1):
    p.append(i)

sumOfCost = 0
treeRoots = 0
# sumOfCost: 최소 신장 트리인 간선들의 cost 합계

while treeRoots < n-1:
    x, y, wt = graph[0]
    del graph[0]

    # 루트 노드가 서로 다르면 최소 신장 트리에 추가
    # 루트 노드가 서로 다르다는 것은 서로 이어도 사이클이 발생하지 않는다는 것임
    if find(x) != find(y):
        union(x, y)
        mst.append((x, y)) 
        sumOfCost += wt
        treeRoots += 1

# 최소 신장 트리를 노드1부터 순서대로 보여줌
mst.sort(key = lambda x: x[0])

# 최소 신장 트리의 간선들을 출력
print('Minimum Spanning Tree :', end=' ')

if len(mst) > 0:
    print(mst[0][0], '-', mst[0][1], end='')

    for i in range(1,len(mst)):
        print(',', mst[i][0], '-', mst[i][1], end='')
    
    print()
else:
    print('None')

# 최소 신장 트리의 cost 합계를 출력
print('Total Cost :', sumOfCost)

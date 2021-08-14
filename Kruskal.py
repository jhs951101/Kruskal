# n: 총 노드의 수
# graph: 간선 정보들 - [노드A, 노드B, 간선 비용]
n = 7
graph = [[1,2,1],[1,3,4],[2,3,7],[2,4,3],[2,6,10],[3,5,5],[3,6,4],[4,6,6],[4,7,9],[5,6,2],[6,7,8]]

# 해당 노드의 루트 노드(최상위 노드)를 return
def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

# 2개의 트리를 하나로 결합하고 루트 노드도 하나로 변경
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1


mst = []
p = [0]
graph.sort(key = lambda x: x[2])

for i in range(1,n+1):
    p.append(i)

# sumOfCost: 최소 신장 트리인 간선들의 cost 합계
sumOfCost = 0
treeEdges = 0

while treeEdges < n-1:
    u, v, wt = graph[0]
    del graph[0]

    # 루트 노드가 서로 같은지 다른지에 따라 사이클 발생 여부를 알 수 있음
    # 루트 노드가 서로 같을 때 이으면 사이클이 발생하므로 제외 
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v)) 
        sumOfCost += wt
        treeEdges += 1

mst.sort(key = lambda x: x[0])

# 최소 신장 트리인 간선들을 출력
print('Minimum Spanning Tree :', mst)
# 최소 신장 트리인 간선들의 cost 합계를 출력
print('Total Costs :', sumOfCost)

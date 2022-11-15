#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> p(1);

// 해당 노드의 루트 노드(최상위 노드)를 return
int find(int x){
    if(x != p[x])
        p[x] = find(p[x]);

    return p[x];
}

// 2개의 트리를 하나로 결합하고 루트 노드도 하나로 변경
void combine(int x, int y){
    int root1 = find(x);
    int root2 = find(y);
    p[root2] = root1;
}

int main(){
    int n = 7;
    vector<vector<int>> graph = {{1,2,1}, {1,3,4}, {2,3,7}, {2,4,3}, {2,6,10}, {3,5,5}, {3,6,4}, {4,6,6}, {4,7,9}, {5,6,2}, {6,7,8}};
    // n: 총 노드의 수
    // graph: 그래프 내의 간선 정보들 - [노드A, 노드B, 비용]

    vector<vector<int>> mst;
    // mst: 최소 신장 트리

    // 간선 정보들을 비용이 가장 낮은 것부터 정렬
    sort(graph.begin(), graph.end(),
        [](vector<int> first, vector<int> second) -> bool
        {
            return first[2] < second[2];
        }
    );

    for(int i=1; i<n+1; i++)
        p.push_back(i);

    int sumOfCost = 0;
    int treeRoots = 0;
    // sumOfCost: 최소 신장 트리인 간선들의 cost 합계

    while(treeRoots < n-1){
        int x = graph[0][0];
        int y = graph[0][1];
        int wt = graph[0][2];
        graph.erase(graph.begin());

        // 루트 노드가 서로 다르면 최소 신장 트리에 추가
        // 루트 노드가 서로 다르다는 것은 서로 이어도 사이클이 발생하지 않는다는 것임
        if(find(x) != find(y)){
            combine(x, y);
            mst.push_back({x, y}); 
            sumOfCost += wt;
            treeRoots += 1;
        }
    }

    // 최소 신장 트리를 노드1부터 순서대로 보여줌
    sort(mst.begin(), mst.end(),
        [](vector<int> first, vector<int> second) -> bool
        {
            return first[0] < second[0];
        }
    );

    // 최소 신장 트리의 간선들을 출력
    cout << "Minimum Spanning Tree : ";

    if(mst.size() > 0){
        cout << mst[0][0] << " - " << mst[0][1];

        for(int i=1; i<mst.size(); i++)
            cout << ", " << mst[i][0] << " - " << mst[i][1];
        
        cout << endl;
    }
    else{
        cout << "None" << endl;
    }

    // 최소 신장 트리의 cost 합계를 출력
    cout << "Total Cost : " << sumOfCost << endl;
    return 0;
}
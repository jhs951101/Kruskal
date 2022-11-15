package pkg;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Kruskal {

    public List<Integer> p = new ArrayList<>(Arrays.asList(0));

    // 해당 노드의 루트 노드(최상위 노드)를 return
    public int find(int x){
        if(x != p.get(x))
            p.set(x, find(p.get(x)));

        return p.get(x);
    }

    // 2개의 트리를 하나로 결합하고 루트 노드도 하나로 변경
    public void combine(int x, int y){
        int root1 = find(x);
        int root2 = find(y);
        p.set(root2, root1);
    }
	
	public void main() {
        int n = 7;
        List<int[]> graph = new ArrayList<>(
        		Arrays.asList(new int[]{1,2,1}, new int[]{1,3,4}, new int[]{2,3,7}, new int[]{2,4,3}, new int[]{2,6,10}, new int[]{3,5,5}, new int[]{3,6,4}, new int[]{4,6,6}, new int[]{4,7,9}, new int[]{5,6,2}, new int[]{6,7,8})
        );
        // n: 총 노드의 수
        // graph: 그래프 내의 간선 정보들 - [노드A, 노드B, 비용]

        List<int[]> mst = new ArrayList<>();
        // mst: 최소 신장 트리

        // 간선 정보들을 비용이 가장 낮은 것부터 정렬
        graph.sort((int[] first, int[] second) -> first[2]-second[2]);

        for(int i=1; i<n+1; i++)
            p.add(i);

        int sumOfCost = 0;
        int treeRoots = 0;
        // sumOfCost: 최소 신장 트리인 간선들의 cost 합계

        while(treeRoots < n-1){
            int x = graph.get(0)[0];
            int y = graph.get(0)[1];
            int wt = graph.get(0)[2];
            graph.remove(0);

            // 루트 노드가 서로 다르면 최소 신장 트리에 추가
            // 루트 노드가 서로 다르다는 것은 서로 이어도 사이클이 발생하지 않는다는 것임
            if(find(x) != find(y)){
                combine(x, y);
                mst.add(new int[]{x, y}); 
                sumOfCost += wt;
                treeRoots += 1;
            }
        }

        // 최소 신장 트리를 노드1부터 순서대로 보여줌
        mst.sort((int[] first, int[] second) -> first[0]-second[0]);

        // 최소 신장 트리의 간선들을 출력
        System.out.print("Minimum Spanning Tree : ");

        if(mst.size() > 0){
            System.out.print(mst.get(0)[0] + " - " + mst.get(0)[1]);

            for(int i=1; i<mst.size(); i++)
                System.out.print(", " + mst.get(i)[0] + " - " + mst.get(i)[1]);
            
            System.out.println();
        }
        else{
            System.out.println("None");
        }

        // 최소 신장 트리의 cost 합계를 출력
        System.out.println("Total Cost : " + sumOfCost);
    }

    public static void main(String[] args) {
    	Kruskal main = new Kruskal();
    	main.main();
    }
}
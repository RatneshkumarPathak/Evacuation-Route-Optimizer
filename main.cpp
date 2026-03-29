#include "graph.h"
#include "algorithms.h"

int main() {
    Graph g(5);

    g.addEdge(0, 1, 4, 2);
    g.addEdge(0, 2, 3, 5);
    g.addEdge(1, 2, 1, 1);
    g.addEdge(1, 3, 7, 3);
    g.addEdge(2, 4, 2, 4);
    g.addEdge(3, 4, 1, 2);

    g.printGraph();
    dijkstra(g, 0);
    return 0;
}
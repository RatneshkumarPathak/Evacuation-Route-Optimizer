#include "graph.h"

Graph::Graph(int V) {
    this->V = V;
    adj.resize(V);
}

void Graph::addEdge(int u, int v, double dist, double risk) {
    adj[u].push_back(Edge(v, dist, risk));
    adj[v].push_back(Edge(u, dist, risk)); // undirected graph
}

void Graph::printGraph() {
    for (int i = 0; i < V; i++) {
        cout << "Node " << i << " -> ";

        for (auto &edge : adj[i]) {
            cout << "(" << edge.to
                 << ", dist=" << edge.distance
                 << ", risk=" << edge.risk
                 << ") ";
        }

        cout << endl;
    }
}

void Graph::blockEdge(int u, int v) {

    for (auto &edge : adj[u]) {
        if (edge.to == v) edge.blocked = true;
    }

    for (auto &edge : adj[v]) {
        if (edge.to == u) edge.blocked = true;
    }
}
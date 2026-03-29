#include "algorithms.h"
#include <queue>
#include <limits>
#include <vector>
#include <iostream>

using namespace std;

void dijkstra(Graph &g, int source, double alpha, double beta) {
    int V = g.V;

    vector<double> dist(V, numeric_limits<double>::max());
    vector<int> parent(V, -1);

    priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> pq;

    // // tuning parameters
    // double alpha = 1.0;  // distance weight
    // double beta = 2.0;   // risk weight

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto &edge : g.adj[u]) {

            if (edge.blocked) continue;

            double cost = alpha * edge.distance + beta * edge.risk;

            if (dist[u] + cost < dist[edge.to]) {
                dist[edge.to] = dist[u] + cost;
                parent[edge.to] = u;

                pq.push({dist[edge.to], edge.to});
            }
        }
    }

    // PRINT RESULT
    cout << "\nDijkstra Result:\n";

    for (int i = 0; i < V; i++) {
        cout << "Node " << i << " cost = " << dist[i] << endl;
    }
}
#ifndef GRAPH_H
#define GRAPH_H

#include <iostream>
#include <vector>
using namespace std;

struct Edge {
    int to;
    double distance;
    double risk;
    bool blocked;

    Edge(int t, double d, double r) {
        to = t;
        distance = d;
        risk = r;
        blocked = false;
    }
};

class Graph {
public:
    int V;
    vector<vector<Edge>> adj;

    Graph(int V);
    void addEdge(int u, int v, double dist, double risk);
    void blockEdge(int u, int v);
    void printGraph();
};

#endif
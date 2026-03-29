import tkinter as tk
from tkinter import simpledialog
import heapq
import math

graph = {}
blocked_edges = set()
node_positions = {}

# =========================
# AUTO NODE POSITIONING
# =========================
def update_positions():
    n = len(graph)
    if n == 0:
        return

    radius = 180
    center_x = 400
    center_y = 250

    nodes = list(graph.keys())

    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / n
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        node_positions[node] = (x, y)

# =========================
# DIJKSTRA
# =========================
def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        for v, distance, risk in graph[u]:
            if (u, v) in blocked_edges or (v, u) in blocked_edges:
                continue

            cost = distance + 2 * risk

            if current_dist + cost < dist[v]:
                dist[v] = current_dist + cost
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent

# =========================
# DRAW GRAPH
# =========================
def draw():
    canvas.delete("all")

    update_positions()

    # Draw edges
    for u in graph:
        for v, d, r in graph[u]:
            if u < v:
                x1, y1 = node_positions[u]
                x2, y2 = node_positions[v]

                is_blocked = (u, v) in blocked_edges or (v, u) in blocked_edges
                color = "red" if is_blocked else "black"
                width = 3 if is_blocked else 1

                canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2
                canvas.create_text(mid_x, mid_y, text=f"{d},{r}", fill="blue")

    # Draw nodes
    for node in graph:
        x, y = node_positions[node]
        canvas.create_oval(x-15, y-15, x+15, y+15, fill="lightblue")
        canvas.create_text(x, y, text=str(node), font=("Arial", 10, "bold"))

# =========================
# ADD EDGE
# =========================
def add_edge():
    u = simpledialog.askinteger("Input", "From node:")
    v = simpledialog.askinteger("Input", "To node:")
    d = simpledialog.askfloat("Input", "Distance:")
    r = simpledialog.askfloat("Input", "Risk:")

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append((v, d, r))
    graph[v].append((u, d, r))

    draw()

# =========================
# TOGGLE EDGE
# =========================
def toggle_edge():
    u = simpledialog.askinteger("Input", "Node 1:")
    v = simpledialog.askinteger("Input", "Node 2:")

    if (u, v) in blocked_edges or (v, u) in blocked_edges:
        blocked_edges.discard((u, v))
        blocked_edges.discard((v, u))
        print(f"Edge {u}-{v} unblocked")
    else:
        blocked_edges.add((u, v))
        print(f"Edge {u}-{v} blocked")

    draw()

# =========================
# RUN DIJKSTRA
# =========================
def run_algo():
    start = simpledialog.askinteger("Input", "Source node:")
    end = simpledialog.askinteger("Input", "Destination node:")

    if start not in graph or end not in graph:
        print("Invalid nodes")
        return

    dist, parent = dijkstra(start)

    path = []
    cur = end

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    print("Path:", path)

    draw()

    # Highlight path
    for i in range(len(path) - 1):
        x1, y1 = node_positions[path[i]]
        x2, y2 = node_positions[path[i+1]]

        canvas.create_line(x1, y1, x2, y2, width=4, fill="green")

# =========================
# UI
# =========================
root = tk.Tk()
root.title("Evacuation Route Visualizer")

canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()

tk.Button(root, text="Add Edge", command=add_edge).pack(side=tk.LEFT)
tk.Button(root, text="Toggle Edge", command=toggle_edge).pack(side=tk.LEFT)
tk.Button(root, text="Run Dijkstra", command=run_algo).pack(side=tk.LEFT)

root.mainloop()
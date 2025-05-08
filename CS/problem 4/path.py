# pip install network // for networkx
'''
import networkx as nx
import matplotlib.pyplot as plt

# Activity list: (Activity Name, Start Node, End Node, Duration)
activities = [
    ('A', 1, 2, 11),  # Build Legs
    ('B', 1, 3, 3),   # Build Top
    ('C', 1, 4, 10),  # Build Drawer
    ('D', 4, 5, 3),   # Paint Drawer
    ('E', 3, 5, 1),   # Paint Top
    ('F', 2, 6, 2),   # Paint Legs
    ('G', 5, 6, 1),   # Attach Drawer to Top
    ('H', 6, 7, 1)    # Attach Legs
]

# Create a directed graph
G = nx.DiGraph()

# Add edges with durations and activity names
for name, start, end, duration in activities:
    G.add_edge(start, end, activity=name, duration=duration)

# Forward Pass - Calculate earliest start and finish times
earliest_start = {}
earliest_finish = {}

for node in nx.topological_sort(G):
    incoming = G.in_edges(node, data=True)

# নোডের দিকে আসা সব ইনকামিং এজ (incoming edges) বের করে।

    if not incoming:
        earliest_start[node] = 0
    else:
        earliest_start[node] = max(earliest_finish[u] for u, _, _ in incoming)
    earliest_finish[node] = earliest_start[node] + max((data['duration'] for _, _, data in incoming), default=0)
#u, _, _ মানে: "আমাকে শুধু source node (u) দাও, বাকি দুইটা ফেলে দাও"
#(source_node, target_node, edge_data_dict)
# Backward Pass - Calculate latest start and finish times
latest_finish = {}
latest_start = {}

# Start from the end node
end_node = max(earliest_finish, key=earliest_finish.get)
latest_finish[end_node] = earliest_finish[end_node]
latest_start[end_node] = latest_finish[end_node]

for node in reversed(list(nx.topological_sort(G))):
    outgoing = G.out_edges(node, data=True)
    if not outgoing:
        latest_finish[node] = earliest_finish[end_node]
    else:
        latest_finish[node] = min(latest_start[v] for _, v, _ in outgoing)
    latest_start[node] = latest_finish[node] - max((data['duration'] for _, _, data in outgoing), default=0)

# Identify critical path
critical_path = []
for u, v, data in G.edges(data=True):
    est = earliest_start[u]
    lst = latest_start[u]
    if est == lst:
        critical_path.append(data['activity'])

# Display results
print("Critical Path Activities:", " → ".join(critical_path))
print("Project Completion Time:", earliest_finish[end_node], "hours")

# Draw the network graph
pos = nx.spring_layout(G)
edge_labels = {(u, v): f"{d['activity']} ({d['duration']}h)" for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Project Network Diagram - Critical Path Method")
plt.show()'''







# pip install networkx matplotlib
import networkx as nx
import matplotlib.pyplot as plt

# Activity list: (Activity Name, Start Node, End Node, Duration)
activities = [
    ('A', 1, 2, 11),  # Build Legs
    ('B', 1, 3, 3),   # Build Top
    ('C', 1, 4, 10),  # Build Drawer
    ('D', 4, 5, 3),   # Paint Drawer
    ('E', 3, 5, 1),   # Paint Top
    ('F', 2, 6, 2),   # Paint Legs
    ('G', 5, 6, 1),   # Attach Drawer to Top
    ('H', 6, 7, 1)    # Attach Legs
]

# Create a directed graph
G = nx.DiGraph()

# Add edges with durations and activity names
for name, start, end, duration in activities:
    G.add_edge(start, end, activity=name, duration=duration)

# Forward Pass - Calculate earliest start and finish times
earliest_start = {}
earliest_finish = {}

for node in nx.topological_sort(G):
    incoming = G.in_edges(node, data=True)
    if not incoming:
        earliest_start[node] = 0
    else:
        earliest_start[node] = max(earliest_finish[u] for u, _, _ in incoming)
    earliest_finish[node] = earliest_start[node] + max((data['duration'] for _, _, data in incoming), default=0)

# Backward Pass - Calculate latest start and finish times
latest_finish = {}
latest_start = {}

end_node = max(earliest_finish, key=earliest_finish.get)
latest_finish[end_node] = earliest_finish[end_node]
latest_start[end_node] = latest_finish[end_node]

for node in reversed(list(nx.topological_sort(G))):
    outgoing = G.out_edges(node, data=True)
    if not outgoing:
        latest_finish[node] = earliest_finish[end_node]
    else:
        latest_finish[node] = min(latest_start[v] for _, v, _ in outgoing)
    latest_start[node] = latest_finish[node] - max((data['duration'] for _, _, data in outgoing), default=0)

# Identify critical path
critical_path = []
for u, v, data in G.edges(data=True):
    est = earliest_start[u]
    lst = latest_start[u]
    if est == lst:
        critical_path.append(data['activity'])

# Display results
print("Node\tES\tEF\tLS\tLF\tST")
for node in G.nodes():
    es = earliest_start[node]
    ef = earliest_finish[node]
    ls = latest_start[node]
    lf = latest_finish[node]
    st = lf - ls
    print(f"{node}\t{es}\t{ef}\t{ls}\t{lf}\t{st}")

print("\nCritical Path Activities:", " → ".join(critical_path))
print("Project Completion Time:", earliest_finish[end_node], "hours")

# Draw the network graph with ES, EF, LS, LF
pos = nx.spring_layout(G, seed=42)

# Node labels with times
node_labels = {
    node: f"{node}\nES:{earliest_start[node]}\nEF:{earliest_finish[node]}\nLS:{latest_start[node]}\nLF:{latest_finish[node]}"
    for node in G.nodes()
}

edge_labels = {(u, v): f"{d['activity']} ({d['duration']}h)" for u, v, d in G.edges(data=True)}

nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=2000, font_weight='bold')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(G, pos, arrows=True)

plt.title("Project Network Diagram - Critical Path Method")
plt.show()

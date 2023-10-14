import networkx as nx
import statistics
# Set the number of nodes
n = 200

# List of different p values
p_values = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]

# Number of graphs to generate for each p
num_graphs_per_p = 200

# Function to generate G(n, p) random graph
def generate_random_graph(n, p):
    G = nx.gnp_random_graph(n, p)
    return G

# Function to calculate the number of connected components
def count_connected_components(graph):
    return nx.number_connected_components(graph)

# Iterate through different p values and generate graphs
all_graphs = []
# Store results in a dictionary
results = {}
for p in p_values:
    connected_components = []
    for _ in range(num_graphs_per_p):
        random_graph = generate_random_graph(n, p)
        all_graphs.append(random_graph) # Computed the 1000 Graphs
        num_components = count_connected_components(random_graph)
        connected_components.append(num_components)

# Calculate average and standard deviation
    avg_components = statistics.mean(connected_components)
    std_deviation = statistics.stdev(connected_components)
    results[p] = {
        "avg": avg_components,
        "std": std_deviation
    }
print(f"Number of graphs: {len(all_graphs)}")

# Now, the results dictionary contains the average and standard deviation for each p value
print("Results:")
for p, data in results.items():
    print(f"p = {p}: Average = {data['avg']}, Standard Deviation = {data['std']}")





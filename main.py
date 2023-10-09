import powerlaw
import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx
import numpy as np
# Solution-02
# Initialize an empty dictionary to store the degree of each author
degree_distribution = {}
rows, cols = [], []
#  co-authorship matrix
#  “i j v”, where i is the row number
# (starting from 1), j is the column number, and v is the value
with open("dblp-co-authors.txt", "r") as file:
    for line in file:
        i, j, v = map(int, line.strip().split())
        # Since it's an unweighted graph, set v to 1 (optional)
        v = 1
        # Increment the degree for both authors i and j
        degree_distribution[i] = degree_distribution.get(i, 0) + v
        degree_distribution[j] = degree_distribution.get(j, 0) + v
        rows.append(i)
        cols.append(j)
        # print(degree_distribution(i,j))
# print(degree_distribution[0][0])
# exit()
# Calculate the degree distribution as a list
# list of the degree values associated with the items in your co-authorship network.
degree_values = list(degree_distribution.values())
print(degree_values)

# P(x)=Cx−γ
# Load the degree distribution data
data = degree_values
# Fit the data to a power-law distribution using MLE
fit = powerlaw.Fit(data, discrete=True)
# Get the power-law exponent (γ)
gamma = fit.alpha

print(gamma)

# Plot the data and the fitted power-law distribution
fig = fit.plot_ccdf(linewidth=3, label='Empirical Data')
fit.power_law.plot_ccdf(ax=fig, color='r', linestyle='--', label=f'Power Law Fit (γ = {gamma:.2f})')

# Customize the plot
plt.title("Degree Distribution and Power Law Fit")
plt.xlabel("Degree (x)")
plt.ylabel("Complementary Cumulative Distribution Function (CCDF)")
plt.legend()
plt.show()

print(f"The power-law exponent (γ) that fits the degree distribution is approximately {gamma:.2f}")

# Solution-03 For clustering co-efficient

num_nodes = max(max(rows), max(cols))
adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
for i, j in zip(rows, cols):
        adjacency_matrix[i - 1][j - 1] = 1  # Convert to 0-based index
print("adjacency matrix")
print(adjacency_matrix)

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(adjacency_matrix)
# Compute the local clustering coefficient for each node
local_clustering_coefficients = nx.clustering(G)

# Compute the average local clustering coefficient
average_clustering_coefficient = sum(local_clustering_coefficients.values()) / len(G)

print(f"Average Local Clustering Coefficient: {average_clustering_coefficient:.4f}")

# Is the network clique-like
# Find all cliques in the graph
cliques = list(nx.find_cliques(G))

# Print the sizes of the cliques
for i, clique in enumerate(cliques, start=1):
    print(f"Clique {i} Size: {len(clique)}")

# Check if any cliques are large (e.g., significantly larger than the average degree)
average_degree = sum(dict(G.degree()).values()) / len(G)
large_cliques = [clique for clique in cliques if len(clique) > average_degree]

if len(large_cliques) > 0:
    print("The network contains large cliques or dense subgraphs, indicating some clique-like behavior.")
else:
    print("The network does not appear to be strongly clique-like.")

# How many vertices have local clustering  coefficient 1.0?
# Compute the local clustering coefficient for each vertex and store it in a dictionary
# local_clustering_coefficients = nx.clustering(G)

# Count the number of vertices with a local clustering coefficient of 1.0
count = sum(1 for coeff in local_clustering_coefficients.values() if coeff == 1.0)

print(f"Number of vertices with a local clustering coefficient of 1.0: {count}")

# Count the number of vertices with a local clustering coefficient of 0
count = sum(1 for coeff in local_clustering_coefficients.values() if coeff == 0.0)

print(f"Number of vertices with a local clustering coefficient of 0.0: {count}")
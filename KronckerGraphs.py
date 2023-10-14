import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency matrix A of the original graph
A = np.array([[1, 1, 1, 0],
              [1, 1, 1, 0],
              [1, 1, 1, 0],
              [0, 0, 1, 0]])

# Initialize G1 with the first-order adjacency matrix (same as A)
G1 = A

# Define the Kronecker product function for graph generation
def kronecker_product(G, A):
    return np.kron(G, A)

# Generate Kronecker graphs of orders 2, 3, and 4
G2 = kronecker_product(G1, A)
G3 = kronecker_product(G2, A)
G4 = kronecker_product(G3, A)

# Visualize the adjacency matrices
plt.figure(figsize=(12, 4))
plt.subplot(141)
plt.imshow(G1, cmap='binary', interpolation='none')
plt.title('G1')
plt.subplot(142)
plt.imshow(G2, cmap='binary', interpolation='none')
plt.title('G2')
plt.subplot(143)
plt.imshow(G3, cmap='binary', interpolation='none')
plt.title('G3')
plt.subplot(144)
plt.imshow(G4, cmap='binary', interpolation='none')
plt.title('G4')
plt.show()

# Create NetworkX graphs for visualization
def plot_graph(adj_matrix, title):
    G = nx.Graph(adj_matrix)
    plt.figure(figsize=(5, 5))
    plt.title(title)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=300, font_size=10, node_color='lightblue')
    plt.show()

# Plot the Kronecker graphs
plot_graph(G1, 'G1')
plot_graph(G2, 'G2')
plot_graph(G3, 'G3')
plot_graph(G4, 'G4')

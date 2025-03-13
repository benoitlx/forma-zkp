#!/home/bleroux/Documents/forma-zkp/.venv/bin/python

import networkx as nx
import matplotlib.pyplot as plt
from random import seed, sample, randint

s = 73 
# random.seed(s)

def create_random_hamiltonian_graph(n, extra_edges=2):
    # Create a cycle graph (which is Hamiltonian)
    G = nx.cycle_graph(n)
    
    # Add extra random edges
    while extra_edges > 0:
        u = randint(0, n-1)
        v = randint(0, n-1)
        if u != v and not G.has_edge(u, v):
            G.add_edge(u, v)
            extra_edges -= 1

    return G

# Parameters
n = 7  # Number of nodes
extra_edges = 5  # Number of extra edges to add

# Create a random Hamiltonian graph
G = create_random_hamiltonian_graph(n, extra_edges)

# Draw the graph
pos = nx.spring_layout(G, seed=s)  # positions for all nodes
plt.figure(figsize=(8, 6))  # Set the figure size

# Draw all edges in the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16, font_color='black', font_weight='bold')

# Highlight the Hamiltonian cycle in red
cycle_edges = [(i, (i + 1) % n) for i in range(n)]  # Get the edges of the cycle
nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='red', width=2)

plt.title("Random Hamiltonian Graph with Cycle Highlighted")
plt.savefig("tmp/graph.png", format="png")
plt.close()  # Close the plot to free up memory

shuffle = lambda x: sample(x, len(x))

with open("tmp/perm", "w") as perm, open("tmp/init", "w") as init, open("tmp/eng", "w") as eng, open("tmp/cache", "w") as hide, open("tmp/sub_aretes", "w") as cycle, open("tmp/c_in_h", "w") as c:
    G = list(G.edges())
    C = list(range(n))

    # cache 
    hide.write("\n\naretes de H\n")
    for _ in G:
        hide.write("  [###]\n")

    # perm
    sigma = shuffle(range(n))
    perm.write(f"sigma = {sigma}")

    H = list(map(lambda e: (sigma[e[0]], sigma[e[1]]), G))
    # init 
    init.write("\naretes de H  <- sigma ->  aretes de G\n")
    eng.write("\naretes de H               aretes de G\n")
    for a, b in zip(H, G):
        init.write(f"   [{a[0]}-{a[1]}]")
        eng.write(f"   [{a[0]}-{a[1]}]")
        init.write(f"                     [{b[0]}-{b[1]}]\n")
        eng.write(f"                     [{b[0]}-{b[1]}]\n")

    # c_in_h
    C_in_H = list(map(lambda x: sigma[x], C))
    c.write("Cycle dans H   ")
    c.write(f"{C_in_H}")

    def cons(u, v, C):
        ret = False 

        n = len(C)
        for i in range(n):
            if u == C[i] and C[(i + 1) % len(C)] == v:
                ret = True 
        
        return ret

    # sub_aretes
    cycle.write("\naretes de H\n")
    for u, v in H:
        if cons(u, v, C_in_H):
            cycle.write(f"   [{u}-{v}]")
        else:
            cycle.write("  [###]")
        cycle.write("\n")



    # P choisit sigma pour générer H
    # sigma = shuffle(range(n))
    # print(sigma)
    # 
    # reveal(H)
    # 
    # # P s'engage à utiliser sigma
    # # on illustre ici le "commitment scheme" en retournant des cartes que V peut suivre du regard
    # print("P retourne les cartes")
    # hide(H)
    # 
    # # V demande de vérifier l'engagement de P
    # print("V demande de vérifier l'engagement de P")
    # print(sigma)
    # reveal(H)
    # 
    # # V demande de vérifier que P connait un cycle Hamiltonien dans H
    # print("V demande de vérifier que P connait un cycle Hamiltonien dans H")
    # print(C_prime)
    # reveal(H)
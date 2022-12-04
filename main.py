import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from WaveFunctionCollapse import findMatches
from Input import getMatrix, Emails, Names, unpack
from Emails import sendTo

matrix = getMatrix()
matches = findMatches(matrix)

chosenMatrix = []

for m in matches:
    row = np.zeros(len(matches))
    row[int(m)] = 1
    chosenMatrix.append(row)

chosenMatrix = np.array(chosenMatrix)

# print(matrix)
print(matches)
matchesNames = unpack(matches, Names)

Subject = 'Secret Santa is here 🎅🏻🎅🏻🎅🏻'

Body = '''
Ciao {FROM},
per questo magico natale dovrai pensare a cosa regalare a {TO}.
Ricorda max 15€!
🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿🎅🏿
'''

for email, From, To in zip(Emails, Names, matchesNames):
    sendTo(email, Subject, Body.format(FROM=From, TO=To))

figNum = 0


def show_graph_with_labels(adjacency_matrix, mylabels):
    global figNum
    plt.figure(figNum)
    figNum += 1
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.DiGraph()
    all_rows = range(0, adjacency_matrix.shape[0])
    for n in all_rows:
        gr.add_node(n)
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=2000, labels=mylabels,
            with_labels=True, font_size=9)


#show_graph_with_labels(matrix, dict(enumerate(Names)))
#show_graph_with_labels(chosenMatrix, dict(enumerate(Names)))
# plt.show()

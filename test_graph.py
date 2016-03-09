#!/usr/bin/env python

import sqlite3
import time
import networkx as nx

db  = sqlite3.connect("starroamer.db")
cur = db.cursor()

G = nx.DiGraph()
start = time.clock()

# Fill link from station to stargate
edge = cur.execute("""
    SELECT fromID, destID, destName, distance
    FROM jump
""")
for A, B, name, dist in edge:
    G.add_edge(A, B, name=name, weight=dist)

print( time.clock() - start )

path = nx.shortest_path(G, source=60004516, target=60003466)
print(path)
print( time.clock() - start )

path = nx.shortest_path(G, source=60004516, target=60003466, weight="weight")
print(path)
print( time.clock() - start )

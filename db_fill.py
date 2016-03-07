#!/usr/bin/env python

import sqlite3
from math import sqrt

import numpy

"""
groupID:
    10: stargate
    15: station
"""

"""select (select solarSystemName from mapSolarSystems where solarSystemID = (select solarSystemID from mapDenormalize where itemID = (select destinationID from mapJumps where stargateID = map.itemID))), solarSystemID, x, y, z from mapDenormalize as map where groupID = 10 and solarSystemID = 30002543;"""


if __name__ != "__main__":
    exit(1)

db = sqlite3.connect("/home/gkr/Doc/eveonline/universeDataDx.db")

c1 = db.cursor()
c2 = db.cursor()
c3 = db.cursor()
params = []

# Fill link from station to stargate
stations = c1.execute("""
    SELECT itemID, solarSystemID, x, y, z
    FROM mapDenormalize WHERE groupID = 15
""")
for station, solarSystem, xs, ys, zs in stations:
    gates = c2.execute("""
        SELECT (
            SELECT destinationID FROM mapJumps
            WHERE stargateID = itemID
        ), x, y, z
        FROM mapDenormalize
        WHERE groupID = 10 AND solarSystemID = ?
    """, (solarSystem,))
    for gate, xg, yg, zg in gates:
        s = numpy.array((xs, ys, zs))
        g = numpy.array((xg, yg, zg))
        dist = numpy.linalg.norm(s-g)
        c3.execute("""
            SELECT solarSystemName FROM mapSolarSystems
            WHERE solarSystemID = (
                SELECT solarSystemID FROM mapDenormalize
                WHERE groupID = 10 AND itemID = ?
            )
        """, (gate,))
        (name,) = c3.fetchone()
        params.append((station, gate, name, dist))
print("ping 1")

# Fill link from gate to gate
gatesA = c1.execute("""
    SELECT itemID, solarSystemID, x, y, z
    FROM mapDenormalize WHERE groupID = 10
""")
for gateA, solarSystem, xa, ya, za in gatesA:
    gatesB = c2.execute("""
        SELECT (
            SELECT destinationID FROM mapJumps
            WHERE stargateID = itemID
        ), x, y, z
        FROM mapDenormalize
        WHERE groupID = 10 AND solarSystemID = ?
    """, (solarSystem,))
    for gateB, xb, yb, zb in gatesB:
        a = numpy.array((xa, ya, za))
        b = numpy.array((xb, yb, zb))
        dist = numpy.linalg.norm(a-b)+1
        c3.execute("""
            SELECT solarSystemName FROM mapSolarSystems
            WHERE solarSystemID = (
                SELECT solarSystemID FROM mapDenormalize
                WHERE groupID = 10 AND itemID = ?
            )
        """, (gateB, ))
        (name,) = c3.fetchone()
        params.append((gateA, gateB, name, dist))
print("ping 2")

# Fill link from gate to station
gates = c1.execute("""
    SELECT itemID, solarSystemID, x, y, z
    FROM mapDenormalize WHERE groupID = 10
""")
for gate, solarSystem, xa, ya, za in gates:
    stations = c2.execute("""
        SELECT itemID, itemName, x, y, z FROM mapDenormalize
        WHERE groupID = 15 AND solarSystemID = ?
    """, (solarSystem,)).fetchall()
    for station, name, xb, yb, zb in stations:
        a = numpy.array((xa, ya, za))
        b = numpy.array((xb, yb, zb))
        dist = numpy.linalg.norm(a-b)+1
        params.append((gate, station, name, dist))

db.close()
db  = sqlite3.connect("starroamer.db")
cur = db.cursor()
cur.executemany("INSERT INTO jump VALUES (?, ?, ?, ?)", params);
db.commit();
db.close();

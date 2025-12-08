from typing import NamedTuple

INPUT_FILE = 'day-8 input.txt'

class Point(NamedTuple):
    x: int
    y: int
    z: int

class Edge(NamedTuple):
    point1: Point
    point2: Point
    cost: int | float

def make_point(line: str) -> Point:
    x, y, z = line.split(',')
    return Point(int(x), int(y), int(z))

def edge_cost(p1: Point, p2: Point) -> int | float:
    return (p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2

def make_edges(nodes: list[Point]) -> list[Edge]:
    edges: list[Edge] = []
    for p_idx, p1 in enumerate(nodes[:-1]):
        for p2 in nodes[p_idx+1:]:
            edges.append(Edge(p1, p2, edge_cost(p1, p2)))
    return edges

def collapse_sets(setlist: list[set[int]]) -> list[set[int]]:
    joined = True
    while joined:
        joined = False
        for idx, set1 in enumerate(setlist[:-1]):
            for set2 in setlist[idx+1:]:
                if not set1.isdisjoint(set2):
                    # there's an overlap
                    set1 |= set2
                    set2.clear()
                    joined = True
        # clear out the empty sets
        setlist = [setval for setval in setlist if setval]
    
    return setlist

with open(INPUT_FILE) as f:
    content = f.read()

nodes: list[Point] = [make_point(line) for line in content.splitlines()]
node_count = len(nodes)
edges = make_edges(nodes)
edges.sort(key=lambda e: e.cost)

# maybe we make the value of the dict a network ID
point_net: dict[Point, int] = {}
network_links: list[set[int]] = []
net_points: list[set[Point]] = []

# one pass
network_serial = 0
for edge in edges:
    if edge.point1 in point_net:
        p1_net_id = point_net[edge.point1]
        if edge.point2 in point_net:
            # both p1 and p2 are in networks.
            # add edge to one of them, doesn't matter which one
            # link the two networks together
            p2_net_id = point_net[edge.point2]
            if p1_net_id != p2_net_id:
                network_links.append({p1_net_id, p2_net_id})
                # and collapse it
                network_links = collapse_sets(network_links)
        else:
            # p1 is in a network, but p2 isn't
            # just add this edge to p1's network
            # log this network to p2
            net_points[p1_net_id].add(edge.point2)
            point_net[edge.point2] = p1_net_id
    else:
        if edge.point2 in point_net:
            p2_net_id = point_net[edge.point2]
            # p1 is not in a network, but p2 is
            # just add this edge to p2's network
            # log this network to p1
            net_points[p2_net_id].add(edge.point1)
            point_net[edge.point1] = p2_net_id
        else:
            # neither p1 nor p2 are in existing networks
            # create a new network
            net_points.append({edge.point1, edge.point2})
            point_net[edge.point1] = network_serial
            point_net[edge.point2] = network_serial
            network_links.append({network_serial})
            network_serial += 1

    if len(network_links) == 1 and len(point_net) == node_count:
        print(edge.point1.x * edge.point2.x)
        break

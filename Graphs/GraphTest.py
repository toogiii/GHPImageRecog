from Graph2 import Graph2

graph_model = {
    "Chicago": [["LA", 10]],
    "LA": [["Chicago", 10]]
    }
test = Graph2(graph_model)
test.add_vertex("Atlanta", ["Chicago", "LA"], [13, 15])
test.add_vertex("NYC", [], [])
print(test.get_vertices())
print(test.get_edges())
print(test.is_reachable("Chicago", "NYC"))
import random


# this just generates some data
def generate_node_data():
    foo = random.randint(10000, 99999)
    bar = f"{random.randint(0, 16**8 - 1):08X}"
    return {"foo": foo, "bar": bar}


class GraphData:

    def __init__(self):
        self._graph = {
            "A": {"data": generate_node_data(), "neighbors": ["B", "C", "D"]},
            "B": {"data": generate_node_data(), "neighbors": ["A", "E", "F"]},
            "C": {"data": generate_node_data(), "neighbors": ["A", "G"]},
            "D": {"data": generate_node_data(), "neighbors": ["A", "H"]},
            "E": {"data": generate_node_data(), "neighbors": ["B", "I"]},
            "F": {"data": generate_node_data(), "neighbors": ["B", "J"]},
            "G": {"data": generate_node_data(), "neighbors": ["C"]},
            "H": {"data": generate_node_data(), "neighbors": ["D"]},
            "I": {"data": generate_node_data(), "neighbors": ["E"]},
            "J": {"data": generate_node_data(), "neighbors": ["F"]},
        }

    def get_node_data(self, node):
        node_info = self._graph.get(node)
        if node_info:
            return node_info["data"]
        return None

    def get_neighbors(self, node):
        node_info = self._graph.get(node)
        if node_info:
            return node_info["neighbors"]
        return []

    def get_all_nodes(self):
        return list(self._graph.keys())


# Create a singleton instance of GraphData.
_graph_data_instance = GraphData()


def initialize():
    return _graph_data_instance

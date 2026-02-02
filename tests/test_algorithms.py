import pytest
from src.node import Node
from src.algorithms import dijkstra

# Mocking a simple 3x3 grid class structure for testing
class MockNode:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []
        
    def __lt__(self, other):
        return False # Required for heapq comparison

def test_dijkstra_straight_line():
    # Setup: 3 Nodes in a line A -> B -> C
    node_a = MockNode(0, 0)
    node_b = MockNode(0, 1)
    node_c = MockNode(0, 2)
    
    # Connect them
    node_a.neighbors = [node_b]
    node_b.neighbors = [node_a, node_c]
    node_c.neighbors = [node_b]
    
    grid = [[node_a, node_b, node_c]]
    
    # Execute
    path = dijkstra(grid, node_a, node_c)
    
    # Assert
    assert len(path) == 2 # Should contain B and C (excluding start usually, or including depends on logic)
    assert path[-1] == node_c
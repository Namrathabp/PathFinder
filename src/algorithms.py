import heapq

def dijkstra(grid, start_node, end_node, draw_callback=lambda: None):
    """
    Finds the shortest path on a weighted grid.
    :param grid: 2D list of Node objects
    :param start_node: The starting Node object
    :param end_node: The target Node object
    :param draw_callback: A function to update the GUI (optional)
    :return: List of nodes representing the path, or empty list if no path
    """
    
    # Priority Queue stores tuples: (current_distance, count, node)
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start_node))
    
    # Track where we came from
    came_from = {}
    
    # Track lowest cost to reach a node (initialize with infinity)
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start_node] = 0
    
    open_set_hash = {start_node}

    while not len(open_set) == 0:
        # Allow the user to quit even while the algorithm is running
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []

        # Pop the node with the lowest distance
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)

        if current == end_node:
            path = reconstruct_path(came_from, end_node)
            end_node.make_end() # Ensure end node stays red
            return path

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (temp_g_score, count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end_node:
                        neighbor.make_open() # Turn node Green/Orange (scanning)
        
        # --- Update the GUI ---
        draw_callback() 

        if current != start_node:
            current.make_barrier() # Visualize visited nodes (Optional: remove this if you prefer different colors)
            # Actually, standard Dijkstra usually marks "Closed" nodes red/closed. 
            # For this visualizer, let's keep visited nodes slightly different or just rely on 'make_open'
            pass 
            
    return []

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        current = came_from[current]
        if current in came_from: # Avoid coloring start node
             current.make_path()
        path.append(current)
    return path
import pygame
import time
from node import Node
from algorithms import dijkstra

WIDTH = 600
HEIGHT = 650 # Increased height to make room for text at the bottom
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra Shortest Path Finder")
pygame.font.init() # Initialize font module

# Colors
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
FONT_SMALL = pygame.font.SysFont('comicsans', 20)
FONT_LARGE = pygame.font.SysFont('comicsans', 40)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw_ui(win, width, time_taken):
    # Draw a white background for the UI area at the bottom
    pygame.draw.rect(win, WHITE, (0, width, width, 50))
    pygame.draw.line(win, BLACK, (0, width), (width, width), 2) # Separator line
    
    if time_taken is None:
        # Default Instructions
        text = FONT_SMALL.render("Left Click: Draw | Right Click: Erase | SPACE: Run | C: Reset", 1, BLACK)
        win.blit(text, (width/2 - text.get_width()/2, width + 15))
    else:
        # Result Display
        result_text = f"Path Found! Time: {time_taken}s (Press C to Reset)"
        text = FONT_SMALL.render(result_text, 1, RED)
        win.blit(text, (width/2 - text.get_width()/2, width + 15))

def draw(win, grid, rows, width, time_taken):
    win.fill(WHITE)
    
    # Draw Nodes
    for row in grid:
        for node in row:
            node.draw(win)
            
    # Draw Grid Lines
    draw_grid(win, rows, width)
    
    # Draw UI Text
    draw_ui(win, width, time_taken)
    
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 30
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    time_taken = None # Store the result time

    while run:
        # Pass time_taken to the draw function
        draw(win, grid, ROWS, width, time_taken)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Prevent drawing if clicked in the UI area (bottom 50px)
            if pygame.mouse.get_pos()[1] > width:
                continue

            # --- MOUSE CONTROLS ---
            if pygame.mouse.get_pressed()[0]: # Left Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # Right Click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.color = WHITE
                if node == start: start = None
                if node == end: end = None

            # --- KEYBOARD CONTROLS ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    start_time = time.time()
                    
                    # We pass a lambda to draw() that allows animation updates
                    # Note: We pass 'None' for time_taken during animation
                    dijkstra(grid, start, end, lambda: draw(win, grid, ROWS, width, None))
                    
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 4)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    time_taken = None # Reset the timer display

    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)
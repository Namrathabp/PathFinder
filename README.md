Dijkstra Shortest Path Visualizer
A robust, interactive Python application that visualizes Dijkstra's Pathfinding Algorithm in real-time. 
This project demonstrates core computer science concepts including graph theory, Object-Oriented Programming (OOP), and algorithmic efficiency analysis.

🚀 Key FeaturesInteractive Grid System: 
Users can draw walls, define start/end points, and create custom mazes using a responsive GUI.
Real-Time Visualization: Animates the "scanning" process of the algorithm (Open Set vs. Closed Set) to visually demonstrate how Dijkstra guarantees the shortest path.
Performance Benchmarking: Includes a built-in timer to measure execution time, allowing for performance analysis of pathfinding complexity.
Engineering-Grade Architecture: Built with a modular OOP design, separating the Node logic, Grid management, and Algorithm implementation.
Unit Testing: Includes a test suite using pytest to validate algorithmic correctness before visual rendering.
🛠️ Tech StackLanguage: Python 3.xGUI 
Framework: PygameTesting: Pytest
Data Structures: Priority Queues (heapq)

📂 Project StructurePlaintextPathfinder_Project/
│
├── src/
│   ├── algorithms.py    # Implementation of Dijkstra's Algorithm using heapq
│   ├── node.py          # Node class managing state (Start, End, Wall, Path)
│   ├── main_viz.py      # Main entry point handling the Pygame UI loop
│   └── __init__.py
│
├── tests/
│   ├── test_algorithms.py # Unit tests for pathfinding logic
│   └── __init__.py
│
├── requirements.txt     # Dependency management
└── README.md            # Project documentation

⚙️ Installation & SetupClone the RepositoryBashgit clone <your-repo-url>
cd Pathfinder_Project
Create a Virtual Environment (Recommended)Bashpython -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install DependenciesBashpip install -r requirements.txt
(If requirements.txt is missing, run: pip install pygame pytest)

Key / Action,Function
Left Click,"Place Start (Green), End (Red), or Walls (Black)"
Right Click,Erase nodes
SPACE Bar,Run the visualization
C Key,Clear board / Reset
<img width="754" height="851" alt="image" src="https://github.com/user-attachments/assets/74e4e5ff-0d0d-428a-8d3e-2cfa67725ca7" />

🧪 Running TestsThis project follows "Test-Driven Development" (TDD) principles. To verify the pathfinding logic without the GUI:Bashpytest

🧠 Algorithmic LogicThis project uses Dijkstra's Algorithm, which guarantees the shortest path in a weighted graph (or an unweighted grid like this one).
Initialization: Set distance to Start Node as 0 and all others as Infinity.
Priority Queue: Use a Min-Heap to explore the node with the shortest known distance first.
Relaxation: For every neighbor of the current node, calculate if the new path is shorter than the previously known path.
Backtracking: Once the End Node is reached, traverse backward using the came_from map to reconstruct the optimal path.

🔮 Future Improvements
Implement A Search Algorithm* for performance comparison (Heuristic-based).
Add "Maze Generation" algorithms (Recursive Division) to auto-build maps.
Add support for weighted nodes (e.g., "mud" tiles that cost more to traverse).

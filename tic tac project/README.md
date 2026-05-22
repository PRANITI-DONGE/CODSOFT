 Tic-Tac-Toe AI Agent — Minimax with Alpha-Beta Pruning

An unbeatable Tic-Tac-Toe AI built in Python using the Minimax algorithm with optional Alpha-Beta Pruning — developed as part of an AI/ML internship project.

 Project Overview :-

This project implements a classic **Human vs AI** Tic-Tac-Toe game where the AI agent is provably unbeatable. The AI uses the Minimax algorithm, a foundational decision-making algorithm in game theory and artificial intelligence, with an optional Alpha-Beta Pruning optimization that dramatically reduces the number of game states evaluated.

The script is designed to run interactively in Google Colab or any standard Python terminal.

Algorithms Implemented :-

1. Minimax Algorithm
- Recursively explores all possible game states
- Alternates between Maximizer (AI) and Minimizer (Human) layers
- Returns the optimal move assuming both players play perfectly
- On the first move, explores up to ~255,168 nodes

2. Minimax with Alpha-Beta Pruning
- Extends Minimax with two pruning bounds:
- Alpha (α) — best score the Maximizer can guarantee
- Beta (β) — best score the Minimizer can guarantee
- Prunes branches where `β ≤ α` (they cannot affect the final decision)
- On the first move, explores as few as ~2,764 nodes — a ~99% reduction
- Produces identical results to plain Minimax, just much faster

Why is the AI unbeatable?
Minimax with perfect play on a 3×3 board is mathematically optimal. The best outcome a human can achieve against the AI is a draw — a win is impossible.

Project Structure :-

tic-tac-toe-ai/
│
├── tic_tac_toe_ai.py   # Main game script (all logic in one file)
└── README.md           # Project documentation


How to Run

Option A — Google Colab
1. Upload 'tic_tac_toe_ai.py' to your Colab session
2. Run in a cell:
python
!python tic_tac_toe_ai.py

Or paste the entire script content into a cell and run it directly.

Option B — Local Terminal
Make sure you have **Python 3.6+** installed (no external libraries needed).
bash
git clone https://github.com/<your-username>/tic-tac-toe-ai.git
cd tic-tac-toe-ai
python tic_tac_toe_ai.py

Gameplay :-

Algorithm options:
  [1] Minimax with Alpha-Beta Pruning  (faster)
  [2] Plain Minimax                    (slower, educational)
Select algorithm (1/2): 1

Choose your symbol:
  [X] — You go first
  [O] — AI goes first
  
Your symbol (X/O): X

Board layout — positions you enter (1–9) map to the board like this:


  7 | 8 | 9
  ──┼───┼──
  4 | 5 | 6
  ──┼───┼──
  1 | 2 | 3


AI move output :-

AI is thinking (O) using Minimax + Alpha-Beta Pruning 
AI chose position 5
Nodes explored : 2,764
Time taken     : 1.243 ms

Performance Comparison :-

Plain Minimax - ~255,168 , ~150 ms 
Minimax + Alpha-Beta Pruning - ~2,764 , ~2 ms 

Values are for the very first move from an empty board on a standard machine.

Key Concepts

Game Tree - All possible sequences of moves represented as a tree 
Terminal State -  Win, loss, or draw — leaf nodes of the game tree 
Static Evaluation - +10 (AI wins), -10 (Human wins), 0 (Draw) 
Depth Penalty - Score adjusted by depth (10 - depth) so AI prefers faster wins 
Pruning - Skipping branches guaranteed not to affect the optimal decision 

Features

-  Human vs AI (choose to play as X or O)
-  Toggle between Minimax and Alpha-Beta Pruning
-  Node counter and timing stats shown after every AI move
-  Clean, readable board display after every turn
-  Replay without restarting the session
-  Zero external dependencies — pure Python standard library

Requirements

- Python 3.6 or higher
- No external packages required (math and time are standard library modules)

References

- Russell, S. & Norvig, P. — Artificial Intelligence: A Modern Approach
- [Minimax Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning — Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)


Author

Praniti Donge
AI/ML Internship Project
GITAM UNIVERSITY

License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

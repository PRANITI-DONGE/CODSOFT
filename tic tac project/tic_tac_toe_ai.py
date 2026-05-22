
"""Tic-Tac-Toe AI Agent — Minimax with Alpha-Beta Pruning"""


import math
import time

# ─────────────────────────────────────────────
# 1. BOARD UTILITIES
# ─────────────────────────────────────────────

def create_board():
    """Return an empty 3×3 board (list of 9 strings)."""
    return [" "] * 9


def display_board(board):
    """Pretty-print the board with position hints."""
    print("\n")
    print(f"  {board[0]} │ {board[1]} │ {board[2]}      7 │ 8 │ 9")
    print("  ──┼───┼──      ──┼───┼──")
    print(f"  {board[3]} │ {board[4]} │ {board[5]}      4 │ 5 │ 6")
    print("  ──┼───┼──      ──┼───┼──")
    print(f"  {board[6]} │ {board[7]} │ {board[8]}      1 │ 2 │ 3")
    print()


def get_available_moves(board):
    """Return list of empty cell indices."""
    return [i for i, cell in enumerate(board) if cell == " "]


def check_winner(board, player):
    """Return True if the given player has won."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # cols
        (0, 4, 8), (2, 4, 6),               # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)


def is_terminal(board):
    """Return True if the game is over (win or draw)."""
    return (
        check_winner(board, "X")
        or check_winner(board, "O")
        or not get_available_moves(board)
    )


def evaluate(board, ai_player, human_player):
    """
    Static evaluation of board state.
      +10  → AI wins
      -10  → Human wins
       0   → Draw / ongoing
    """
    if check_winner(board, ai_player):
        return 10
    if check_winner(board, human_player):
        return -10
    return 0

# 2. MINIMAX ALGORITHM

def minimax(board, depth, is_maximizing, ai_player, human_player, node_counter):
    """
    Plain Minimax (no pruning).

    Parameters
    ----------
    board           : current board state
    depth           : depth of recursion (used for score adjustment)
    is_maximizing   : True when it's the AI's turn
    ai_player       : AI's symbol ('X' or 'O')
    human_player    : Human's symbol
    node_counter    : list[int] — mutable counter for explored nodes

    Returns
    -------
    int : best score from this state
    """
    node_counter[0] += 1

    score = evaluate(board, ai_player, human_player)

    # Terminal states — adjust by depth so AI prefers quicker wins
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not get_available_moves(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_player
            best = max(best, minimax(board, depth + 1, False, ai_player, human_player, node_counter))
            board[move] = " "
        return best
    else:
        best = math.inf
        for move in get_available_moves(board):
            board[move] = human_player
            best = min(best, minimax(board, depth + 1, True, ai_player, human_player, node_counter))
            board[move] = " "
        return best

# 3. MINIMAX WITH ALPHA-BETA PRUNING

def minimax_ab(board, depth, is_maximizing, alpha, beta, ai_player, human_player, node_counter):
    """
    Minimax with Alpha-Beta Pruning.

    alpha : best score the maximizer can guarantee so far
    beta  : best score the minimizer can guarantee so far

    Branches are pruned when alpha >= beta, skipping
    subtrees that cannot influence the final decision.
    """
    node_counter[0] += 1

    score = evaluate(board, ai_player, human_player)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not get_available_moves(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_player
            best = max(best, minimax_ab(board, depth + 1, False, alpha, beta, ai_player, human_player, node_counter))
            board[move] = " "
            alpha = max(alpha, best)
            if beta <= alpha:          # ← Beta cut-off (prune remaining branches)
                break
        return best
    else:
        best = math.inf
        for move in get_available_moves(board):
            board[move] = human_player
            best = min(best, minimax_ab(board, depth + 1, True, alpha, beta, ai_player, human_player, node_counter))
            board[move] = " "
            beta = min(beta, best)
            if beta <= alpha:          # ← Alpha cut-off (prune remaining branches)
                break
        return best

# 4. AI MOVE SELECTOR


def get_ai_move(board, ai_player, human_player, use_alpha_beta=True):
    """
    Find the best move for the AI using the selected algorithm.

    Returns
    -------
    (best_move, nodes_explored, elapsed_time)
    """
    best_score = -math.inf
    best_move = None
    node_counter = [0]

    start = time.perf_counter()

    for move in get_available_moves(board):
        board[move] = ai_player

        if use_alpha_beta:
            score = minimax_ab(board, 0, False, -math.inf, math.inf,
                               ai_player, human_player, node_counter)
        else:
            score = minimax(board, 0, False,
                            ai_player, human_player, node_counter)

        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    elapsed = time.perf_counter() - start
    return best_move, node_counter[0], elapsed

# 5. HUMAN INPUT

def get_human_move(board):
    """
    Prompt the human for a valid move (1–9, mapped to board index 0–8).
    Board positions shown to user:
        7 | 8 | 9
        4 | 5 | 6
        1 | 2 | 3
    """
    pos_to_index = {
        1: 6, 2: 7, 3: 8,
        4: 3, 5: 4, 6: 5,
        7: 0, 8: 1, 9: 2,
    }
    while True:
        try:
            choice = int(input("Your move (1-9): "))
            if choice not in pos_to_index:
                print("  ✗ Enter a number between 1 and 9.")
                continue
            idx = pos_to_index[choice]
            if board[idx] != " ":
                print("  ✗ That cell is already taken. Try again.")
                continue
            return idx
        except ValueError:
            print("  ✗ Invalid input. Enter a number between 1 and 9.")


# 6. GAME LOOP


def play_game():
    print("=" * 55)
    print("   TIC-TAC-TOE — Minimax AI Agent (Internship Project)")
    print("=" * 55)

    # ── Choose algorithm ──
    print("\nAlgorithm options:")
    print("  [1] Minimax with Alpha-Beta Pruning  (faster)")
    print("  [2] Plain Minimax                    (slower, educational)")
    while True:
        algo = input("Select algorithm (1/2): ").strip()
        if algo in ("1", "2"):
            break
        print("  ✗ Enter 1 or 2.")
    use_alpha_beta = (algo == "1")
    algo_name = "Minimax + Alpha-Beta Pruning" if use_alpha_beta else "Plain Minimax"
    print(f"  ✓ Using: {algo_name}\n")

    # ── Choose symbol ──
    print("Choose your symbol:")
    print("  [X] — You go first")
    print("  [O] — AI goes first")
    while True:
        symbol = input("Your symbol (X/O): ").strip().upper()
        if symbol in ("X", "O"):
            break
        print("  ✗ Enter X or O.")

    human_player = symbol
    ai_player = "O" if symbol == "X" else "X"
    print(f"  ✓ You are '{human_player}', AI is '{ai_player}'\n")

    # ── Determine turn order ──
    # X always starts first in classic Tic-Tac-Toe
    current_turn = "X"

    board = create_board()
    display_board(board)

    # ── Main game loop ──
    while not is_terminal(board):
        if current_turn == human_player:
            print(f"--- Your turn ({human_player}) ---")
            move = get_human_move(board)
            board[move] = human_player
        else:
            print(f"--- AI is thinking ({ai_player}) using {algo_name} ---")
            move, nodes, elapsed = get_ai_move(board, ai_player, human_player, use_alpha_beta)
            board[move] = ai_player
            # Convert internal index back to user-friendly position
            index_to_pos = {6: 1, 7: 2, 8: 3, 3: 4, 4: 5, 5: 6, 0: 7, 1: 8, 2: 9}
            print(f"  AI chose position {index_to_pos[move]}")
            print(f"  Nodes explored : {nodes:,}")
            print(f"  Time taken     : {elapsed*1000:.3f} ms")

        display_board(board)
        current_turn = "O" if current_turn == "X" else "X"

    # ── Result ──
    print("=" * 55)
    if check_winner(board, human_player):
        print("   Congratulations! You won! (That should not happen...)")
    elif check_winner(board, ai_player):
        print("  AI wins! The Minimax AI is unbeatable.")
    else:
        print("  It's a Draw! Well played.")
    print("=" * 55)



# 7. ENTRY POINT WITH REPLAY


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye \n")
            break


if __name__ == "__main__":
    main()

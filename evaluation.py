"""Heuristic evaluation from the requested player's perspective."""

from config import RED, BLACK, RED_KING, BLACK_KING
from game.moves import get_valid_moves


def evaluate(board, player=BLACK):

    # Base score is BLACK-positive and RED-negative.
    score = 0

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece == RED:
                score -= 100
                score -= (7 - row) * 5

            elif piece == BLACK:
                score += 100
                score += row * 5

            elif piece == RED_KING:
                score -= 175

            elif piece == BLACK_KING:
                score += 175

            if piece != 0 and 2 <= col <= 5:
                score += 3 if piece < 0 else -3

    black_mobility = len(get_valid_moves(board, BLACK))
    red_mobility = len(get_valid_moves(board, RED))

    score += 2 * (black_mobility - red_mobility)

    # Convert BLACK-positive score to requested player's perspective.
    return score * (-player)

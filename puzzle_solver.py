"""Resolución del 8-puzzle por búsqueda en profundidad (DFS)."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Iterable, List, Optional, Tuple

Board = Tuple[int, ...]
Move = str


@dataclass
class SearchResult:
    found: bool
    nodes_explored: int
    solution_moves: List[Move] = field(default_factory=list)
    reason: str = ""


def parse_board(values: Iterable[int]) -> Board:
    board = tuple(int(v) for v in values)
    if len(board) != 9:
        raise ValueError("El tablero debe tener exactamente 9 celdas.")
    if sorted(board) != list(range(9)):
        raise ValueError("El tablero debe contener los dígitos 0-8 sin repetir.")
    return board


def board_key(board: Board) -> Board:
    return board[:9]


def blank_index(board: Board) -> int:
    return board.index(0)


def apply_move(board: Board, move: Move) -> Board:
    idx = blank_index(board)
    cells = list(board[:9])

    if move == "arriba" and idx >= 3:
        swap = idx - 3
    elif move == "abajo" and idx <= 5:
        swap = idx + 3
    elif move == "izquierda" and idx % 3 != 0:
        swap = idx - 1
    elif move == "derecha" and idx % 3 != 2:
        swap = idx + 1
    else:
        raise ValueError(f"Movimiento inválido: {move}")

    cells[idx], cells[swap] = cells[swap], cells[idx]
    return tuple(cells)


def legal_moves(board: Board) -> List[Move]:
    idx = blank_index(board)
    moves: List[Move] = []
    if idx >= 3:
        moves.append("arriba")
    if idx <= 5:
        moves.append("abajo")
    if idx % 3 != 0:
        moves.append("izquierda")
    if idx % 3 != 2:
        moves.append("derecha")
    return moves


def format_board(board: Board) -> str:
    rows = [board[i : i + 3] for i in range(0, 9, 3)]
    return "\n".join(" ".join(str(cell) for cell in row) for row in rows)


def dfs_solve(initial: Board, goal: Board, max_depth: int) -> SearchResult:
    if max_depth < 0:
        raise ValueError("La profundidad máxima no puede ser negativa.")

    if initial == goal:
        return SearchResult(found=True, nodes_explored=1, solution_moves=[])

    # DFS iterativo con pila (LIFO) — orden correcto para profundidad.
    stack: Deque[Tuple[Board, List[Move]]] = deque([(initial, [])])
    visited: set[Board] = {initial}
    nodes_explored = 0

    while stack:
        board, moves = stack.pop()
        nodes_explored += 1

        if len(moves) >= max_depth:
            continue

        for move in legal_moves(board):
            next_board = apply_move(board, move)
            if next_board in visited:
                continue

            next_moves = moves + [move]
            if next_board == goal:
                return SearchResult(
                    found=True,
                    nodes_explored=nodes_explored,
                    solution_moves=next_moves,
                )

            visited.add(next_board)
            stack.append((next_board, next_moves))

    return SearchResult(
        found=False,
        nodes_explored=nodes_explored,
        reason=f"Sin solución dentro de profundidad {max_depth}.",
    )

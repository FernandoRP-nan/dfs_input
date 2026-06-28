#!/usr/bin/env python3
"""CLI del buscador de caminos (8-puzzle con DFS)."""

from __future__ import annotations

import argparse
import sys

from puzzle_solver import SearchResult, dfs_solve, format_board, parse_board


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resuelve el 8-puzzle con búsqueda en profundidad (DFS).",
    )
    parser.add_argument(
        "--initial",
        required=True,
        help="Estado inicial: 9 dígitos separados por coma (0 = vacío). Ej: 1,2,3,4,5,6,7,0,8",
    )
    parser.add_argument(
        "--final",
        required=True,
        help="Estado objetivo con el mismo formato. Ej: 1,2,3,4,5,6,7,8,0",
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=20,
        help="Profundidad máxima de búsqueda (default: 20).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Muestra tableros intermedios de la solución.",
    )
    return parser


def parse_cli_board(raw: str) -> tuple[int, ...]:
    parts = [p.strip() for p in raw.split(",")]
    if len(parts) != 9:
        raise ValueError(f"Se esperaban 9 valores, recibidos {len(parts)}.")
    return parse_board(int(p) for p in parts)


def print_result(result: SearchResult, initial: tuple[int, ...], goal: tuple[int, ...], verbose: bool) -> None:
    print("Estado inicial:")
    print(format_board(initial))
    print("\nEstado objetivo:")
    print(format_board(goal))
    print(f"\nNodos explorados: {result.nodes_explored}")

    if not result.found:
        print(f"\n❌ {result.reason or 'No se encontró solución.'}")
        return

    print(f"\n✅ Solución encontrada en {len(result.solution_moves)} movimientos:")
    print(" → ".join(result.solution_moves) if result.solution_moves else "(ya estaba resuelto)")

    if verbose and result.solution_moves:
        board = initial
        print("\nSecuencia:")
        for step, move in enumerate(result.solution_moves, start=1):
            from puzzle_solver import apply_move

            board = apply_move(board, move)
            print(f"\nPaso {step} ({move}):")
            print(format_board(board))


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        initial = parse_cli_board(args.initial)
        goal = parse_cli_board(args.final)
        result = dfs_solve(initial, goal, args.depth)
        print_result(result, initial, goal, args.verbose)
        return 0 if result.found else 1
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

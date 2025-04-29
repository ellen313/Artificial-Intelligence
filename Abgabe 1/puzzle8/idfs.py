# idfs.py
# ------------------------------------------
# Author: Ellen Peppmüller, Begüm Peker
# Datum: 21.03.2025
# Beschreibung: Implementierung der Iterativen Tiefensuche für
# das 8-Puzzle-problem.py.
# ------------------------------------------

from board import Board
from collections import deque


def dfs(cur_board, path, limit, visited):
    """
    TODO: Implementiere die Rekursive Tiefensuche mit Limitierung.
    """
    # states_count = 0
    if cur_board.is_solved():  # Puzzle in einem Zielzustand?
        return path
    if limit == 0:
        return None  # maximale zulässige Rekursionstiefe erreicht

    for child in cur_board.possible_actions():
        if child in visited:
            continue
        # states_count += 1
        path.append(child)
        visited.add(child)
        result = dfs(child, path, limit - 1, visited)
        if result is not None:
            return result
        path.pop()
        visited.remove(child)

    return None


def idfs(start_board: Board, limit=1000):  # max. Tiefe arbiträr gesetzt
    """
    Iterative Tiefensuche mit Schleife zur Erhöhung des Tiefenlimits.
    Gibt den Lösungspfad als deque zurück oder None, wenn keine Lösung gefunden
    wurde.
    """
    for depth in range(limit):
        path = deque([start_board])
        visited = set()
        result = dfs(start_board, path, depth, visited)
        if result:
            return result
    return None

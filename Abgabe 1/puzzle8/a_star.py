# board.py
# ------------------------------------------
# Author: Ellen Peppmüller, Begüm Peker
# Datum: 21.03.2025
# Beschreibung: Template für die Implementierung des A* Algorithmus
# ------------------------------------------
import heapq
from collections import deque
from board import Board
from typing import Optional


class Node:
    """
    Repräsentiert einen Knoten im Suchbaum für den A*-Algorithmus.

    Attribute:
        board (Board): Der aktuelle Zustand des Spielfelds.
        parent (Node, optional): Der Vorgängerknoten (Elternknoten) in der Pfadsuche.
        g (int): Die bisherigen Pfadkosten von Start bis zu diesem Knoten.
        h (int): Der geschätzte Abstand zum Zielzustand (Heuristik).
        f (int): Die geschätzten Gesamtkosten f = g + h.
    """

    def __init__(self, board: Board, parent: 'Node' = None, g=0):
        self.board = board
        self.parent = parent
        self.g = g  # Pfadkosten
        self.h = board.h2()  # Heuristikwert
        self.f = self.g + self.h  # f = g + h

    def __lt__(self, other):
        """
        Vergleichsmethode für die Prioritätswarteschlange.
        Knoten mit kleineren f-Werten werden bevorzugt.
        """
        return self.f < other.f  # Für PriorityQueue


def reconstruct_path(node: Node) -> deque[Board]:
    """
    Rekonstruiert den Pfad vom Startzustand bis zum Zielzustand.
    TODO: Implementiere das erstellen des Pfades.
    """
    path = deque()
    while node:
        path.appendleft(node.board)
        node = node.parent
    return path


def a_star(start_board: Board) -> Optional[deque[Board]]:
    """
    Führt den A*-Algorithmus zur Lösung des 8-Puzzle-Problems aus.
    TODO: Implementiere den A*-Algorithmus.
    Es empfiehlt sich hierbei heapq für die open_list und set() für die
    closed_list zu verwenden.
    """
    open_list = []
    heapq.heappush(open_list, Node(start_board))
    closed_list = set()

    states_count = 0

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.board.is_solved():
            print(f"Anzahl der generierten Zustände: {states_count}")
            return reconstruct_path(current_node)

        closed_list.add(current_node.board)

        for action in current_node.board.possible_actions():
            if action in closed_list:
                continue

            g_new = current_node.g + 1
            h_new = action.h2()
            node = Node(action, current_node, g_new)

            if all(node.f < n.f for n in open_list if n.board == action):  # testen ob gleiches board nur kürzerer wert
                heapq.heappush(open_list, node)  # neuen besseren knoten hinzufügen

                states_count += 1

    print(f"Anzahl der generierten Zustände: {states_count}")
    return None  # Kein Pfad gefunden

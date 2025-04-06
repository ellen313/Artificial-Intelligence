
# board.py
# ------------------------------------------
# Author: Ellen Peppmüller, Begüm Peker
# Datum: 21.03.2025
# Beschreibung: Implementierung der Board-Klasse für das 8-Puzzle-Problem.
# ------------------------------------------
import random


class Board:
    """
    Repräsentiert ein 8-Puzzle-Board.

    Methoden:
    - parity(): Prüft, ob das Puzzle lösbar ist.
    - h1(), h2(): Platzhalter für Heuristikfunktionen.
    - possible_actions(): Liefert gültige Nachfolgezustände.
    - is_solved(): Prüft, ob das Ziel erreicht ist.
    """

    N = 8  # Problemgröße

    def __init__(self, board=None):
        """
        Initialisiert das Board.
        Wenn kein Board übergeben wird, wird ein zufälliges, lösbares Board
        erzeugt.
        """
        if board:
            self.board = list(board)
        else:
            self.board = list(range(1, Board.N + 2))
            while True:
                self.board = list(range(Board.N + 1))
                if self.parity():
                    break

    def __str__(self):
        """
        Gibt das Board als String aus.
        """
        return f"Puzzle{{board={self.board}}}"

    def __eq__(self, other):
        """
        Zwei Boards sind gleich, wenn ihr Zustand gleich ist.
        """
        return isinstance(other, Board) and self.board == other.board

    def __hash__(self):
        """
        Ermöglicht das Nutzen von Board in Sets oder als Dictionary-Keys.
        """
        return hash(tuple(self.board))

    def parity(self):
        """
        Paritätsprüfung:
        Gibt True zurück, wenn das Board lösbar ist.
        TODO: Implementiere die Berechnung der Parität
        """
        #parity_counter = 0
        #new_board = self.board.copy()
        #n = len(self.board)
        #for i in range(n):
        #    for j in range(n - i - 1):
        #        if new_board[j] > new_board[j + 1]:
        #            # new_board[j], new_board[j + 1] = new_board[j + 1], new_board[j] #parallele Zuweisung
        #            parity_counter += 1
        #return parity_counter

        false_count = 0
        for i in range(1, len(self.board)):
            for j in self.board:
                if j == 0:
                    continue
                if j > i:
                    false_count += 1
                if j == i:
                    break

        #return false_count
        return false_count % 2 == 0



    def h1(self):
        """
        Heuristikfunktion h1 (siehe Aufgabenstellung).
        TODO: Implementiere einfache Heuristik
        """
        result = 0
        for i in range(len(self.board)):
            if self.board[i] == 0:
                continue
            if self.board[i] != i:
                result += 1
        return result

    def h2(self):
        """
        Heuristikfunktion h2 (siehe Aufgabenstellung).
        TODO: Implementiere verbesserte Heuristik
        """
        result = 0
        for i in range(len(self.board)):
            if self.board[i] == 0:
                continue

            row, col = divmod(i, 3)
            goal_row, goal_col = divmod(self.board[i], 3)

            result += abs(row - goal_row) + abs(col - goal_col)

        return result

    def possible_actions(self):
        """
        Gibt eine Liste aller möglichen Folge-Boards zurück,
        die durch einen gültigen Zug entstehen.
        TODO: Diese Methode muss noch implementiert werden.
        """
        # Postion im Puzzle
        zero_index = self.board.index(0)
        row, col = divmod(zero_index, 3)

        moves = []

        # nach oben (Zeile - 1)
        if row > 0:
            new_board = self.board[:]
            new_board[zero_index], new_board[zero_index - 3] = new_board[zero_index - 3], new_board[zero_index] # tausch der Werte
            moves.append(Board(new_board))

        # nach unten (Zeile + 1)
        if row < 2:
            new_board = self.board[:]
            new_board[zero_index], new_board[zero_index + 3] = new_board[zero_index + 3], new_board[zero_index]
            moves.append(Board(new_board))

        # nach links (Spalte - 1)
        if col > 0:
            new_board = self.board[:]
            new_board[zero_index], new_board[zero_index - 1] = new_board[zero_index - 1], new_board[zero_index]
            moves.append(Board(new_board))

        # nach rechts (Spalte + 1)
        if col < 2:
            new_board = self.board[:]
            new_board[zero_index], new_board[zero_index + 1] = new_board[zero_index + 1], new_board[zero_index]
            moves.append(Board(new_board))

        return moves

    def is_solved(self):
        """
        Prüft, ob das Board im Zielzustand ist (0,1,2,3,...,8).
        TODO: Implementiere die Prüfung ob das Board gelöst ist.
        """
        return self.board == list(range(len(self.board)))


def main():
    b = Board([7, 2, 4, 5, 0, 6, 8, 3, 1])  # Startzustand manuell setzen
    # b = Board()  # Lösbares Puzzle zufällig generieren
    print("Startzustand:", b)

    print("Parität:", b.parity())

    print("Heuristik h1: ", b.h1())
    print("Heuristik h2: ", b.h2())

    for child in b.possible_actions():
        print(child)

    print("Ist gelöst:", b.is_solved())


if __name__ == "__main__":
    main()

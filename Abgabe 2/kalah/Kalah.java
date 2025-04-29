import java.util.List;

/**
 * Hauptprogramm für KalahMuster.
 *
 * @since 29.3.2021
 * @author oliverbittel
 */
public class Kalah {

    private static final String ANSI_BLUE = "\u001B[34m";

    private static int min = 0;
    private static int max = 0;
    private static int turns = 0;
    private static final boolean HEURISTIC = true;
    private static final int DEPTH = 10;


    /**
     *
     * @param args wird nicht verwendet.
     */
    public static void main(String[] args) {
        //testExample();
        //testHHGame();
        testMiniMaxAndAlphaBetaWithGivenBoard();
        //testHumanMiniMax();
        //testHumanMiniMaxAndAlphaBeta();
    }


    /**
     * Beispiel von https://de.wikipedia.org/wiki/Kalaha
     */
    public static void testExample() {
        KalahBoard kalahBd = new KalahBoard(new int[]{5, 3, 2, 1, 2, 0, 0, 4, 3, 0, 1, 2, 2, 0}, 'B');
        kalahBd.print();

        System.out.println("B spielt Mulde 11");
        kalahBd.move(11);
        kalahBd.print();

        System.out.println("B darf nochmals ziehen und spielt Mulde 7");
        kalahBd.move(7);
        kalahBd.print();
    }

    /**
     * Mensch gegen Mensch
     */
    public static void testHHGame() {
        KalahBoard kalahBd = new KalahBoard();
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action = kalahBd.readAction();
            kalahBd.move(action);
            kalahBd.print();
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");
    }

    public static void testMiniMaxAndAlphaBetaWithGivenBoard() {
        min = 0;
        max = 0;
        turns = 0;


        KalahBoard kalahBd = new KalahBoard(new int[]{2, 0, 4, 3, 2, 0, 0, 1, 0, 1, 3, 2, 1, 0}, 'A');
        // A ist am Zug und kann aufgrund von Bonuszügen 8-aml hintereinander ziehen!
        // A muss deutlich gewinnen!
        kalahBd.print();

        while (!kalahBd.isFinished()) {
            int action;
            if (kalahBd.getCurPlayer() == 'A') {
                // Berechnen Sie für A eine Aktion mit Ihrem Verfahren und geben Sie die Aktion auf der Konsole aus.
                //action = maxActionAlphaBetaSearch(kalahBd).getLastPlay();
                action = maxAction(kalahBd).getLastPlay();
                System.out.println(ANSI_BLUE + "Bester Zug für A: " + action);
            } else {
                action = kalahBd.readAction();
            }
            action = kalahBd.readAction();
            kalahBd.move(action);
            kalahBd.print();
            turns++;
        }

        System.out.println("\n" + ANSI_BLUE + "GAME OVER");

        int aScore = kalahBd.getAKalah();
        int bScore = kalahBd.getBKalah();
        System.out.println("Endstand A: " + aScore + " | B: " + bScore);

        if (aScore > bScore) {
            System.out.println("Spieler A hat gewonnen!");
        } else if (bScore > aScore) {
            System.out.println("Spieler B hat gewonnen!");
        } else {
            System.out.println("Unentschieden!");
        }

        System.out.println("Züge insgesamt: " + turns);
        System.out.println("Ø Min-Aufrufe: " + (min / (double) turns));
        System.out.println("Ø Max-Aufrufe: " + (max / (double) turns));

    }

    /** Min-Max-Suche*/

    private static KalahBoard maxAction(KalahBoard state) {
        if (state.isFinished()) {
            return state;
        }

        int v = Integer.MIN_VALUE;
        KalahBoard action = state;

        for (KalahBoard currBoard : state.possibleActions()) {
            if (currBoard.isBonus()) {
                int v1 = maxValue(currBoard, DEPTH);
                if (v1 > v)
                    v = v1;
                action = currBoard;
            } else {
                int v1 = minValue(currBoard, DEPTH);
                if (v1 > v) {
                    v = v1;
                    action = currBoard;
                }
            }
        }
        return action;
    }

    private static int minValue(KalahBoard kalahBd, int depth) {
        min++;

        if (kalahBd.isFinished() || depth <= 0) {
            return evaluate(kalahBd);
        }

        int v = Integer.MAX_VALUE;

        for (KalahBoard currBoard : kalahBd.possibleActions()) {
            if (currBoard.isBonus()) {
                v = Math.min(v, minValue(currBoard, depth));
            } else {
                v = Math.min(v, maxValue(currBoard, depth - 1));
            }
        }
        return v;
    }

    private static int maxValue(KalahBoard board, int depth) {
        max++;

        if (board.isFinished() || depth <= 0) {
            return evaluate(board);
        }

        int v = Integer.MIN_VALUE;

        for (KalahBoard currBoard : board.possibleActions()) {
            if (currBoard.isBonus()) {
                v = Math.max(v, maxValue(currBoard, depth));
            } else {
                v = Math.max(v, minValue(currBoard, --depth));
            }
        }
        return v;
    }

    /**Alpha-Beta-Suche*/

    public static KalahBoard maxActionAlphaBetaSearch(KalahBoard board) {
        if (board.isFinished()) {
            return board;
        }

        int v = Integer.MIN_VALUE; // aktueller bester Wert
        KalahBoard action = board; // aktuell bestes Board

        List<KalahBoard> possibleActions = board.possibleActions();
        if (HEURISTIC) {
            // Züge absteigend nach Bewertung sortieren
            possibleActions.sort((a, b) -> evaluate(b) - evaluate(a));
        }

        for (KalahBoard currBoard : possibleActions) {
            int v1;
            if (currBoard.isBonus()) {
                v1 = maxValueAlphaBetaSearch(currBoard, DEPTH, Integer.MIN_VALUE, Integer.MAX_VALUE);
            } else {
                v1 = minValueAlphaBetaSearch(currBoard, DEPTH, Integer.MIN_VALUE, Integer.MAX_VALUE);
            }
            if (v1 > v) {
                v = v1; // wenn neuer Wert besser -> merken
                action = currBoard;
            }
        }
        return action; // besten gefundenen Spielstand zurückgeben
    }

    private static int maxValueAlphaBetaSearch(KalahBoard board, int depth, int alpha, int beta){
        max++;

        if (board.isFinished() || depth <= 0) {
            return evaluate(board);
        }

        int v = Integer.MIN_VALUE;

        List<KalahBoard> possibleActions = board.possibleActions();
        if (HEURISTIC) {
            possibleActions.sort((a, b) -> evaluate(b) - evaluate(a));
        }

        for (KalahBoard currBoard : possibleActions) {
            if (currBoard.isBonus()) {
                v = Math.max(v, maxValueAlphaBetaSearch(currBoard, depth, alpha, beta));
            } else {
                v = Math.max(v, minValueAlphaBetaSearch(currBoard, --depth, alpha, beta));
            }
            if (v >= beta) // Min bereits in anderem Zweig Wert gefunden
                return v;
            alpha = Math.max(alpha, v);
        }

        return v;
    }

    private static int minValueAlphaBetaSearch(KalahBoard board, int depth, int alpha, int beta){
        min++;

        if (board.isFinished() || depth <= 0) {
            return evaluate(board);
        }

        int v = Integer.MAX_VALUE;

        List<KalahBoard> possibleActions = board.possibleActions();
        if (HEURISTIC) {
            possibleActions.sort((a, b) -> evaluate(a) - evaluate(b));
        }

        for (KalahBoard currBoard : possibleActions) {
            if (currBoard.isBonus()) {
                v = Math.min(v, minValueAlphaBetaSearch(currBoard, depth, alpha, beta));
            } else {
                v = Math.min(v, maxValueAlphaBetaSearch( currBoard, --depth, alpha, beta));
            }
            if (v <= alpha)
                return v;
            beta = Math.min(beta, v);
        }

        return v;
    }

    private static Integer evaluate(KalahBoard board) {
        if (board.getCurPlayer() == 'A') {
            return board.getAKalah() - board.getBKalah();
        }
        else {
            return board.getBKalah() - board.getAKalah();
        }
    }
}

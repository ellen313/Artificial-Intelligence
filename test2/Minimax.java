package aufgaben.Aufgabe2;

import java.util.Comparator;
import java.util.List;

public class Minimax {

    //static int deep = 0;
    static int maxDeep = 8;
    static int minMaxAlphaBetaCounter = 0;

    public static int maxAction(KalahBoard board) {
        minMaxAlphaBetaCounter = 0;
        if (board.isFinished()) return -1;
        int v = Integer.MIN_VALUE;
        int alpha = Integer.MIN_VALUE;
        int beta = Integer.MAX_VALUE;
        KalahBoard res = null;
        for (KalahBoard child: board.possibleActions()) {
            int v1 = child.isBonus() ? maxValue(child, alpha, beta, 0) : minValue(child, alpha, beta,  1);
            if (v1 > v) {
                v = v1;
                res = child;
            }
        }
        return res == null ? -1 : res.getLastPlay();
    }

    static int maxValue(KalahBoard board, int alpha, int beta, int deep) {
        minMaxAlphaBetaCounter++;
        if (board.isFinished() || deep == maxDeep)
            return board.h1();
        int v = Integer.MIN_VALUE;
        List<KalahBoard> sortedActions = board.possibleActions();
        sortedActions.sort((a, b) -> Integer.compare(b.h1(), a.h1()));

        for (KalahBoard child : sortedActions) {
            v = Math.max(v, child.isBonus() ? maxValue(child, alpha, beta, deep) : minValue(child, alpha, beta, deep+1));
            if (v >= beta) return v;
            alpha = Math.max(alpha, v);
        }
        return v;
    }

    static int minValue(KalahBoard board, int alpha, int beta, int deep) {
        minMaxAlphaBetaCounter++;
        if (board.isFinished() || deep == maxDeep) return board.h1();
        int v = Integer.MAX_VALUE;

        List<KalahBoard> sortedActions = board.possibleActions();
        sortedActions.sort((a, b) -> Integer.compare(b.h1(), a.h1()));

        for (KalahBoard child: sortedActions) {
            v = Math.min(v, child.isBonus() ? minValue(child, alpha, beta, deep) : maxValue(child, alpha, beta, deep+1));
            if (v <= alpha) return v;
            beta = Math.min(beta, v);
        }
        return v;
    }
}

from pieces.piece import Piece

class Knight(Piece):

    def __init__(self, color, rank, file):
        super().__init__('N', color, rank, file)

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board

        :param board: current board (see game.py)
        :return: list of (rank, file) tuples
        """
        possible_moves = []
        possible_move_candidates = [
            (self.rank + 2, self.file + 1),
            (self.rank + 2, self.file - 1),
            (self.rank - 2, self.file + 1),
            (self.rank - 2, self.file - 1),

            (self.rank + 1, self.file + 2),
            (self.rank + 1, self.file - 2),
            (self.rank - 1, self.file + 2),
            (self.rank - 1, self.file - 2),
        ]

        # prune invalid moves
        for move in possible_move_candidates:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                if board[move[0]][move[1]] is None or \
                    board[move[0]][move[1]].get_color() != self.color:
                    possible_moves.append(move)

        return possible_moves

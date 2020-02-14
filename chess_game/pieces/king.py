from pieces.piece import Piece


class King(Piece):

    def __init__(self, color, rank, file):
        super().__init__('K', color, rank, file)

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board

        NOTE: THE KING MAY OR MAY NOT BE UNDER CHECK AFTER THESE MOVES

        :param board: current board (see game.py)
        :return: list of (rank, file) tuples
        """
        possible_moves = []

        rank_start, rank_end = max(self.rank - 1, 0), min(self.rank + 1, 7)
        file_start, file_end = max(self.file - 1, 0), min(self.file + 1, 7)

        for i in range(rank_start, rank_end + 1):
            for j in range(file_start, file_end + 1):
                if board[i][j] is None or board[i][j].get_color() != self.color:
                    possible_moves.append((i, j))

        return possible_moves

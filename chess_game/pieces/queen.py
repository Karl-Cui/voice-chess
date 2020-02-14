from pieces.piece import Piece


class Queen(Piece):

    def __init__(self, color, rank, file):
        super().__init__('Q', color, rank, file)

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board

        :param board: current board (see game.py)
        :return: list of (rank, file) tuples
        """
        possible_moves = []

        # search in each direction for possible squares to move to
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            possible_moves.extend(
                self._get_possible_moves_in_dir(board, rank_incr=direction[0], file_incr=direction[1])
            )

        return possible_moves

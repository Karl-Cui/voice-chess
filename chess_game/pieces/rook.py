from pieces.piece import Piece


class Rook(Piece):

    def __init__(self, color, rank, file):
        super().__init__('R', color, rank, file)

    def get_possible_moves(self, board):
        pass

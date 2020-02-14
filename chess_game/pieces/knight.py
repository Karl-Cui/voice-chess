from pieces.piece import Piece

class Knight(Piece):

    def __init__(self, color, rank, file):
        super().__init__('N', color, rank, file)

    def get_possible_moves(self, board):
        pass

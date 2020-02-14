from pieces.piece import Piece

class Pawn(Piece):

    def __init__(self, color, rank, file):
        super().__init__('P', color, rank, file)

    def get_possible_moves(self, board):
        pass

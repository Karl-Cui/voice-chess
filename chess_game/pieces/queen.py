from pieces.piece import Piece

class Queen(Piece):

    def __init__(self, color, rank, file):
        super().__init__('Q', color, rank, file)

    def get_possible_moves(self, board):
        pass

from pieces.piece import Piece

class King(Piece):

    def __init__(self, color, rank, file):
        super().__init__('K', color, rank, file)

    def get_possible_moves(self, board):
        pass

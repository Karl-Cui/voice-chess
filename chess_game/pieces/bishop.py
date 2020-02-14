from pieces.piece import Piece

class Bishop(Piece):

    def __init__(self, color, rank, file):
        super().__init__('B', color, rank, file)

    def get_possible_moves(self, board):
        pass

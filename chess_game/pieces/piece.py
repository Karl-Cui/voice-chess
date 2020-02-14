class Piece():

    def __init__(self, piece, color, rank, file):
        """
        Create a piece.

        :param piece: piece (P, N, B, R, Q, K)
        :param color: 0 for white, 1 for black
        :param rank: rank of piece (0-7)
        :param file: file of piece (0-7)
        :return: None
        """
        self.piece = piece
        self.color = color

        self.rank = rank
        self.file = file

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board
        """
        pass

    #
    #   Getters and setters
    #

    def get_piece(self, case=False):
        """
        Get current piece (P, N, B, R, Q, K).

        :param case: if True, return uppercase piece for white and lowercase
                     for black
        :return: None
        """
        if self.color == 0 or not case:
            return self.piece
        return self.piece.lower()

    def get_color(self):
        return self.color

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def get_file(self, file):
        self.file = file

class Piece:

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

        self.moved = False

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board

        :param board: current board (see game.py)
        :return: list of (rank, file) tuples
        """
        pass    # to be implemented by each individual class

    def _get_possible_moves_in_dir(self, board, rank_incr, file_incr):
        """
        Get all possible moves in a certain direction

        :param board: current board (see game.py
        :param rank_incr: how much to increment rank every step (-1, 0, 1)
        :param file_incr: how much to increment file every step (-1, 0, 1)
        :return: list of (rank, file) tuples
        """
        possible_moves = []

        new_rank = self.rank + rank_incr
        new_file = self.file + file_incr

        # keep incrementing / decrementing rank and file until we encounter the
        # edge of the board or another piece
        while 0 <= new_rank <= 7 and 0 <= new_file <= 7:

            if board[new_rank][new_file] is None:
                possible_moves.append((new_rank, new_file))
            else:
                if board[new_rank][new_file].get_color() != self.color:
                    possible_moves.append((new_rank, new_file))
                break

            new_rank += rank_incr
            new_file += file_incr

        return possible_moves

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

    def get_file(self):
        return self.file

    def set_file(self, file):
        self.file = file

    def get_moved(self):
        return self.moved

    def set_moved(self):
        self.moved = True

from pieces.piece import Piece

class Pawn(Piece):

    def __init__(self, color, rank, file):
        super().__init__('P', color, rank, file)

    def get_possible_moves(self, board):
        """
        Return all possible squares to move to in (rank, file) form given the
        current board

        :param board: current board (see game.py)
        :return: list of (rank, file) tuples
        """
        possible_moves = []

        #
        # if pawn is white
        #

        if self.color == 0:

            # check square in front of it
            if board[self.rank + 1][self.file] is None:
                possible_moves.append((self.rank + 1, self.file))

                # check 2 squares in front of it if the pawn is on the 2nd file
                if self.rank == 1 and board[self.rank + 2][self.file] is None:
                    possible_moves.append((self.rank + 2, self.file))

            # check for captures
            for incr in [-1, 1]:
                if 0 <= self.file + incr <= 7 and \
                    board[self.rank + 1][self.file + incr] is not None:

                    if board[self.rank + 1][self.file + incr].get_color() == 1:
                        possible_moves.append((self.rank + 1, self.file + incr))

        #
        # if pawn is black
        #

        else:

            # check square in front of it
            if board[self.rank - 1][self.file] is None:
                possible_moves.append((self.rank - 1, self.file))

                # check 2 squares in front of it if the pawn is on the 2nd file
                if self.rank == 6 and board[self.rank - 2][self.file] is None:
                    possible_moves.append((self.rank - 2, self.file))

            # check for captures
            for incr in [-1, 1]:
                if 0 <= self.file + incr <= 7 and \
                    board[self.rank - 1][self.file + incr] is not None:

                    if board[self.rank - 1][self.file + incr].get_color() == 0:
                        possible_moves.append((self.rank - 1, self.file + incr))

        return possible_moves

from pieces import *


class ChessGame():

    def __init__(self):
        """
        TODO: option to start game with FEN and stuff
        """
        self.board = None
        self.turn = None        # 0 for white, 1 for black

        self.pieces = [{}, {}]  # first dict for white pieces, second for black
        self._letter_to_file = {ch: i for i, ch in enumerate('abcdefgh')}

    def new_game(self):
        """
        Start new game
        """
        self.board = [[None] * 8 for _ in range(8)]

        # set up pieces
        for rank in [0, 7]:
            self.board[rank][0] = Rook(color=rank % 2, rank=rank, file=0)
            self.board[rank][1] = Knight(color=rank % 2, rank=rank, file=1)
            self.board[rank][2] = Bishop(color=rank % 2, rank=rank, file=2)

            self.board[rank][5] = Bishop(color=rank % 2, rank=rank, file=5)
            self.board[rank][6] = Knight(color=rank % 2, rank=rank, file=6)
            self.board[rank][7] = Rook(color=rank % 2, rank=rank, file=7)

        # set up king and queens
        self.board[0][3] = Queen(color=0, rank=0, file=3)
        self.board[0][4] = King(color=0, rank=0, file=4)
        self.board[7][3] = King(color=1, rank=7, file=3)
        self.board[7][4] = Queen(color=1, rank=7, file=4)

        # set up pawns
        for file in range(8):
            self.board[1][file] = Pawn(color=0, rank=1, file=file)
            self.board[6][file] = Pawn(color=1, rank=6, file=file)

        # gather all pieces
        self._update_pieces()

        # white to move
        self.turn = 0

    def display_board(self, type='print'):
        """
        Display current board state

        :param type: type of board to return
        :return: board (if type is print, return None)
        """
        if self.board is None:
            return

        # print board
        if type == 'print':
            self._print_board()
            return

    #
    #   Move handling
    #

    def move(self, move):
        """
        Process a move

        :param move: move in chess notation
        :return: 0 if move is valid, else -1
        """
        if move == 'O-O-O' or move == 'O-O':
            # TODO: stuff for castling
            pass

        dst = move[-2:]
        dst_file = self._letter_to_file[dst[0]]  # convert letters to indices
        dst_rank = int(dst[1]) - 1               # chess notation is 1-indexed

        # TODO: stuff for en passent

        # TODO: case handling for multiple pieces that can go to a square

    def possible_moves(self, piece, board):
        """
        Lists all possible moves given a piece and a board
        """


    #
    #   Private helper methods
    #

    def _update_pieces(self):
        """
        Updates self.pieces to include every piece on the board

        :return: None
        """
        if self.board is None:
            return

        # reset pieces
        self.pieces = [{}, {}]

        # get all pieces on board
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:

                    piece = self.board[i][j]
                    c = piece.get_color()
                    p = piece.get_piece()
                    self.pieces[c][p] = self.pieces[c].get(p, [])
                    self.pieces[c][p].append(piece)

    def _print_board(self):
        """
        Prints board

        :return None:
        """
        # print backwards, since we want to print black at the top and
        # white at the bottom
        for i in range(7, -1, -1):
            print('---------------------------------')

            for j in range(8):
                piece = self.board[i][j]

                # determine whether to display a piece or a blank square
                if piece is not None:
                    piece = piece.get_piece(case=True)
                else:
                    piece = ' '

                print('| ' + piece + ' ', end='')

            print('|')

        print('---------------------------------')


if __name__ == '__main__':
    game = ChessGame()
    game.new_game()

    game.display_board()

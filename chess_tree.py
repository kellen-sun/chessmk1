import chess
board = chess.Board()
print(board)
board.legal_moves.count()
for x in board.legal_moves:
    board.push_san(x)

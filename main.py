from textwrap import dedent
from gen_img import gen_board, gen_take
import chess


def display_board(c_board: chess.Board):
    board = dedent('''\
           ┌───┬───┬───┬───┬───┬───┬───┬───┐
         8 │ . │ # │ . │ # │ . │ # │ . │ # │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         7 │ # │ . │ # │ . │ # │ . │ # │ . │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         6 │ . │ # │ . │ # │ . │ # │ . │ # │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         5 │ # │ . │ # │ . │ # │ . │ # │ . │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         4 │ . │ # │ . │ # │ . │ # │ . │ # │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         3 │ # │ . │ # │ . │ # │ . │ # │ . │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         2 │ . │ # │ . │ # │ . │ # │ . │ # │
           ├───┼───┼───┼───┼───┼───┼───┼───┤
         1 │ # │ . │ # │ . │ # │ . │ # │ . │
           └───┴───┴───┴───┴───┴───┴───┴───┘
             a   b   c   d   e   f   g   h  ''')

    f_board = ''

    light_sq = []
    dark_sq = []
    
    i = 0
    for g in board:
        x = board.find('.', i)
        if x != -1:
            light_sq.append(x)
            i = x + 1
    i = 0
    for g in board:
        x = board.find('#', i)
        if x != -1:
            dark_sq.append(x)
            i = x + 1
        

    
    

    all_sq = light_sq + dark_sq
    all_sq.sort()
    

    pboard = list(str(c_board).replace(" ", "").replace("\n", ""))
    pieces = [chess.Piece.unicode_symbol(chess.Piece.from_symbol(x)) if x != '.' else '' for x in pboard]

    

    
    z = 0
    for i in range(len(board)):
        if i in all_sq:
            if pieces[z] == '':
                f_board += board[i]
                z += 1
            else:
                f_board += pieces[z]
                z += 1
        else:
            f_board += board[i]

    gen_board(f_board)


def parse_move(board: chess.Board, move: str) -> chess.Move:
    try:
        return board.parse_san(move)
    except:
        move = move.lower()
        return board.parse_uci(move)

def display_take(w_capture,b_capture):
    Captures = 'W : ' + str(w_capture) + '\n\nB : ' + str(b_capture)
    gen_take(Captures)


board = chess.Board()
w_capture = []
b_capture = []

display_board(board)
display_take(w_capture,b_capture)
print(board)



while not board.is_game_over():
    

    if board.turn:
        print("It is currently White's move")
        
    else:
        print("It is currently Black's move")
        

    
    player_input = input('Input your move or \'forfeit\' to forfeit:\n').replace(' ','')


    if player_input.lower() != 'forfeit':
        try:
            p_move = parse_move(board,player_input)
            print(board.piece_at(p_move.to_square))
            if p_move in board.legal_moves:
                if board.is_capture(p_move):
                    cap = board.piece_at(p_move.to_square)
                    if cap.color:
                        b_capture.append(cap.unicode_symbol())
                        display_take(w_capture,b_capture)
                    else:
                        w_capture.append(cap.unicode_symbol())
                        display_take(w_capture,b_capture)
                board.push(p_move)
                display_board(board)
                print(board)
                

            else:
                print(player_input + " Is not a valid move! Please try again\n")

        except Exception as e:
            print(e)
            print('\n Please try again')
    else:
        if board.turn:
            print('White has forfeited\n The winner is: Black')
            break
        else:
            print('Black has forfeited\nThe winner is: White')
            break
    
else:
    if board.outcome().winner:
        winner = 'White'
    elif board.outcome().winner == None:
        winner = 'None'
    else:
        winner = 'Black'
    print('The winner is: ' + winner)
    print('The game ended due to: ' + board.outcome().termination.name)
    







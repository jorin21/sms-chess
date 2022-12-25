from textwrap import dedent
from gen_img import gen_board
import chess


def display_board(c_board):
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


def parse_move(board,move):
    try:
        return board.parse_san(move)
    except:
        move = move.lower()
        return board.parse_uci(move)

board = chess.Board()
display_board(board)
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
            if p_move in board.legal_moves: 
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
    







orig_board = ['-','-','-','-','-','-','-','-','-']

winning_combos = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

def print_board():
    line1 = [orig_board[i] for i in range(len(orig_board)) if i < 3 ]
    line2 = [orig_board[i] for i in range(len(orig_board)) if i > 2 and i < 6 ]
    line3 = [orig_board[i] for i in range(len(orig_board)) if i > 5 and i < 9 ]
    print(f'\n{line3}\n{line2}\n{line1}\n')

def check_win(check_board,current_player):
    for combo in winning_combos:
        result = [check_board[i] for i in combo]
        if "".join(result) == f"{current_player}{current_player}{current_player}":
            return True
        elif round==8:
            print('Draw game!')
            break

def check_opposite():
    # get all empty box
    empty = [i for i in range(len(orig_board)) if orig_board[i] == "-"]
    for spot in empty:
        clone = orig_board.copy()
        clone[spot] = "O"
        if check_win(clone,"O"):
            # to win
            return spot  
    for spot in empty:
        clone = orig_board.copy()
        clone[spot] = "X"
        if check_win(clone,"X"):
            # to block
            return spot
    # if human take 2&6 or 0&8 then need to take 1,3,5,7 to block human
    xSpot = [i for i in range(len(orig_board)) if orig_board[i] == "X"]
    if 2 in xSpot and 6 in xSpot:
        for spot in empty:
            if spot == 1 or spot == 3 or spot == 5 or spot == 7:
                return spot
    elif 0 in xSpot and 8 in xSpot:
        for spot in empty:
            if spot == 1 or spot == 3 or spot == 5 or spot == 7:
                return spot
    for spot in empty:
        if spot == 4:
            # to get middle spot
            return spot
    for spot in empty:
        if spot == 0 or spot == 2 or spot == 6 or spot == 8:
            # to get corner
            return spot
        else:
            return spot
              
for round in range(0,9):
    if round%2 ==0:
        player = 'X'
        print(f"Human {player}:\n============")
        while True:
            try:
                x = int(input("Put in your X coordinate(0-2):\n"))
                y = int(input("Put in your Y coordinate(0-2):\n"))
                if orig_board[y*3+x] == '-':
                    break    
                print("This coordinate is occupied. Please choose again.")
            except IndexError:
                print("Hey, it's outta the tic-tac-toe board! Please choose again.")
            except ValueError:
                print("Only accept integer. Please choose from 1 to 3.")
        orig_board[y*3+x] = player
        
    else:
        player = 'O'
        print(f"Computer {player}:\n============")
        spot = check_opposite()
        orig_board[spot] = player
        
        
    print_board()
    if check_win(orig_board,player) == True:
        print(f'{player} is won')
        break



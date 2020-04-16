def user_choice(board_a, user_no):
    sym = ['X', 'Y']
    pos = input('Enter the position on the board (x,y): ').split(',')
    x, y = tuple(list(map(int, pos)))
    board_a[x][y] = sym[user_no]
    return board_a


def winner_check(board_b):
    # Row check
    for row in board_b:
        if (row.count(row[0]) == len(row)) and row[0] != 0:
            return True

    # Column check
    for x in range(3):
        col = []
        for row in board_b:
            col.append(row[x])
        if (col.count(col[0]) == len(col)) and col[0] != 0:
            return True

    # Diagonal Check
    c = 0
    d = 2
    d1 = []
    d2 = []
    for row in board_b:
        d1.append(row[c])
        d2.append(row[d])
        c += 1
        d -= 1
    if d1.count(d1[0]) == len(d1) and d1[0] != 0:
        return True
    elif d2.count(d2[0]) == len(d2) and d2[0] != 0:
        return True

    return False


def main():
    print('Welcome to tic tac toe!')
    start = input('Start the game? Y/N: ')
    if start.lower() == "y":

        # Creating & displaying a board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        print('   0', ' 1', ' 2')
        for count, row in enumerate(board):
            print(count, row)

        for x in range(9):
            player_no = x % 2
            print("\nPlayer {}: ".format(player_no + 1))
            board = user_choice(board, player_no)
            for each in board:
                print(each)
            if winner_check(board):
                print('\nPlayer {} has won!'.format(player_no + 1))
                break
            elif x == 8:
                print('No Winner!')
    print('\n Thank you for playing')
    return None


main()

field = [['-' for j in range(3)] for i in range(3)]


# Print initial game board
def start_field():
    for n in field:
        print(*n)
    print('---------------------------')


# Player switch generator
def change_player():
    n = 0
    while True:
        if n:
            n += 1
            player = 'o'
        else:
            n -= 1
            player = 'x'
        yield player


# Player move input
def my_input(player):
    print(f"Player {player}'s turn")
    print('---------------------------')
    x = 0
    y = 0
    while True:
        while not (1 <= x <= 3):
            try:
                x = int(input('Choose a row (1 to 3): '))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Invalid input")
            else:
                print(f"You selected row {x}")
        while not (1 <= y <= 3):
            try:
                y = int(input('Choose a column (1 to 3): '))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Invalid input")
            else:
                print(f"You selected column {y}")
        yield x, y


# Validate move
def check(next_move, player):
    move = field[next_move[0] - 1][next_move[1] - 1]
    if move == '-':
        print('---------------------------')
        print(f'Cell {next_move} is free')
        print('Move allowed')
        print('---------------------------')
        move = player
        return next_move, move
    elif move != '-':
        print('---------------------------')
        print(f'Cell {next_move} is already occupied!')
        print('Move not allowed!')
        print('Please try again')
        print('---------------------------')
        next_move = next(my_input(player))
        fix = check(next_move, player)
        return fix


# Update and print game board after move
def output_field(next_move, move):
    field[next_move[0] - 1][next_move[1] - 1] = move
    start_field()


# Check game result
def check_result(player):
    i = 0
    j = 0
    n = 0
    if field[i][i] == field[i + 1][i + 1] == field[i + 2][i + 2] == player:
        print('---------------------------')
        print(f'3 "{player}" on the main diagonal')
        return player

    if field[i + 2][i] == field[i + 1][i + 1] == field[i][i + 2] == player:
        print('---------------------------')
        print(f'3 "{player}" on the secondary diagonal')
        return player

    for i in range(3):
        if '-' not in field[i]:
            n += 1
        if field[i][j] == field[i][j + 1] == field[i][j + 2] == player:
            print('---------------------------')
            print(f'3 "{player}" in row {i + 1}')
            return player
        if field[j][i] == field[j + 1][i] == field[j + 2][i] == player:
            print('---------------------------')
            print(f'3 "{player}" in column {i + 1}')
            return player

    if n == 3:
        print('---------------------------')
        print('Draw')
        return 'No one'

# Game wrapper
def game(func):
    def wrapper():
        print("Game board")
        start_field()
        print(f'{func()} won!')
        print("Game over")
        # Pause for executable version
        input('Press Enter to exit')

    return wrapper


# Main game loop
@game
def main_play():
    val = change_player()
    result = None
    while not result:
        player = next(val)
        next_move = next(my_input(player))
        check_next_move = check(next_move, player)
        output_field(*check_next_move)
        result = check_result(player)
    return result


# Start game
def run_game():
    main_play()

if __name__ == "__main__":
    run_game()
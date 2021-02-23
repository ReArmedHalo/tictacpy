from TicTacToe import TicTacToe
import pytest

# Validate we get a win condition for rows
def test_win_row():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'O', 2: 'X', 3: 'O'},
                 2: {1: 'X', 2: 'X', 3: 'X'},
                 3: {1: 'X', 2: 'O', 3: 'O'}
                 }
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ttt.check_for_win()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Validate we get a win condition for columns
def test_win_column():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'X', 3: 'O'},
                 2: {1: 'X', 2: 'O', 3: 'X'},
                 3: {1: 'X', 2: 'O', 3: 'X'}
                 }
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ttt.check_for_win()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    
# Validate we get a win condition for diagonals
def test_win_diagonal():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: 'X'},
                 2: {1: 'O', 2: 'X', 3: 'O'},
                 3: {1: 'O', 2: 'O', 3: 'X'}
                 }
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ttt.check_for_win()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# We should receive a DRAW if the final move wasn't a winning move
def test_win_draw_no_spaces_left():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: 'X'},
                 2: {1: 'O', 2: 'X', 3: 'O'},
                 3: {1: 'O', 2: 'X', 3: 'O'}
                 }
    ttt.SPACES_LEFT = 0
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ttt.check_for_win()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

# We should receive a WIN if the final move was a winning move
def test_win_last_move():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: 'X'},
                 2: {1: 'O', 2: 'X', 3: 'O'},
                 3: {1: 'O', 2: 'X', 3: 'X'}
                 }
    ttt.SPACES_LEFT = 0
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ttt.check_for_win()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Can't touch this! - We should fail if we try to place a tile over an existing tile
def test_cannot_place_over_another_tile():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: ' '},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    ttt.GAME_STATE = ttt.STATES.CROSS_TURN
    assert ttt.place_marker("X", 1, 1) == False

# Jeffrey! Wait your turn! - We should fail if we try to play the wrong marker during that turn
def test_my_turn():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: ' '},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    ttt.GAME_STATE = ttt.STATES.CROSS_TURN
    assert ttt.place_marker("O", 1, 1) == False
    assert ttt.GAME_STATE == ttt.STATES.CROSS_TURN

# Wait, this isn't tenis! - We should fail if we try to place a marker outside the grid
def test_out_of_bounds():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: ' '},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    ttt.GAME_STATE = ttt.STATES.CROSS_TURN
    assert ttt.place_marker("X", 4, 4) == False
    assert ttt.GAME_STATE == ttt.STATES.CROSS_TURN

# That's illegal! - We should be only be receiving valid input
def test_valid_input_marker():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: ' '},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    ttt.GAME_STATE = ttt.STATES.CROSS_TURN
    assert ttt.place_marker("Y", 2, 2) == False
    assert ttt.GAME_STATE == ttt.STATES.CROSS_TURN
    
def test_place_marker():
    ttt = TicTacToe()
    ttt.board = {1: {1: 'X', 2: 'O', 3: ' '},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    ttt.GAME_STATE = ttt.STATES.CROSS_TURN
    assert ttt.place_marker("X", 1, 3)
    newBoard = {1: {1: 'X', 2: 'O', 3: 'X'},
                 2: {1: ' ', 2: ' ', 3: ' '},
                 3: {1: ' ', 2: ' ', 3: ' '}
                 }
    assert ttt.GAME_STATE == ttt.STATES.NAUGHT_TURN
    assert ttt.board == newBoard

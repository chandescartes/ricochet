from components import Direction, Game


def test_move_up(standard_game_few_walls):
    position = standard_game_few_walls.move_robot(Direction.UP, 8, 8, [])
    assert position == (3, 8)

    position = standard_game_few_walls.move_robot(Direction.UP, 8, 8, [(5, 8)])
    assert position == (6, 8)

    position = standard_game_few_walls.move_robot(
        Direction.UP, 8, 8, [(0, 8), (4, 4), (3, 8), (5, 8), (10, 8)]
    )
    assert position == (6, 8)


def test_move_right(standard_game_few_walls):
    position = standard_game_few_walls.move_robot(Direction.RIGHT, 8, 8, [])
    assert position == (8, 12)

    position = standard_game_few_walls.move_robot(Direction.RIGHT, 8, 8, [(8, 12)])
    assert position == (8, 11)

    position = standard_game_few_walls.move_robot(
        Direction.RIGHT, 8, 8, [(8, 14), (4, 4), (8, 3), (8, 11), (8, 10)]
    )
    assert position == (8, 9)


def test_move_down(standard_game_few_walls):
    position = standard_game_few_walls.move_robot(Direction.DOWN, 8, 8, [])
    assert position == (12, 8)

    position = standard_game_few_walls.move_robot(Direction.DOWN, 8, 8, [(9, 8)])
    assert position == (8, 8)

    position = standard_game_few_walls.move_robot(
        Direction.DOWN, 8, 8, [(13, 8), (4, 4), (3, 8), (11, 8), (10, 8)]
    )
    assert position == (9, 8)


def test_move_left(standard_game_few_walls):
    position = standard_game_few_walls.move_robot(Direction.LEFT, 8, 8, [])
    assert position == (8, 3)

    position = standard_game_few_walls.move_robot(Direction.LEFT, 8, 8, [(8, 5)])
    assert position == (8, 6)

    position = standard_game_few_walls.move_robot(
        Direction.LEFT, 8, 8, [(8, 3), (4, 4), (8, 11), (8, 5), (8, 4)]
    )
    assert position == (8, 6)


def test_encode_robot_positions():
    robot_positions = [(8, 8), (0, 8), (8, 0), (10, 8), (5, 5)]
    result = ((8, 8), (0, 8), (5, 5), (8, 0), (10, 8))
    encoding = Game.encode_robot_positions(robot_positions)
    assert encoding == result

    robot_positions = [(15, 15), (0, 8), (8, 0), (0, 5), (5, 5)]
    result = ((15, 15), (0, 5), (0, 8), (5, 5), (8, 0))
    encoding = Game.encode_robot_positions(robot_positions)
    assert encoding == result


def test_solve_mini(mini_game):
    assert mini_game.solve() == 1

    mini_game.target_position = (3, 2)
    assert mini_game.solve() == 3


def test_solve_standard(standard_game):
    standard_game.initial_robot_positions = [(12, 11), (4, 2), (5, 8), (7, 14)]
    standard_game.target_position = (9, 13)
    assert standard_game.solve() == 9

    standard_game.initial_robot_positions = [(4, 2), (12, 11), (5, 8), (7, 14)]
    standard_game.target_position = (13, 5)
    assert standard_game.solve() == 5

    standard_game.initial_robot_positions = [(5, 8), (4, 2), (12, 11), (7, 14)]
    standard_game.target_position = (3, 6)
    assert standard_game.solve() == 4

    standard_game.initial_robot_positions = [(7, 14), (4, 2), (12, 11), (5, 8)]
    standard_game.target_position = (14, 10)
    assert standard_game.solve() == 4

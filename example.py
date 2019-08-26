from simulator.game import Game
from simulator.agent import Agent
from simulator.board import Board


if __name__ == "__main__":
    # Points & Tiled
    points = [
        [-1, 4, 3, 5, 9, 5, 3, 4, -1],
        [5, 3, 8, -10, 2, -10, 8, 3, 5],
        [6, 3, 7, 8, 0, 8, 7, 4, 6],
        [5, 3, 8, -10, 2, -10, 8, 3, 5],
        [-1, 4, 3, 5, 9, 5, 3, 4, -1]
    ]
    tiled = [
        [0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 2, 0, 0]
    ]

    # Board(width, height, points, tiled)
    board = Board(9, 5, points, tiled)

    # Agent(TeamID, AgentID, x, y)
    ## Note : The coordinate value is 0 standard
    ## Note : AgentID must be unique value!!
    agents = [
        Agent(1, 1, 2, 0),
        Agent(1, 2, 6, 0),
        Agent(1, 3, 4, 1),
        Agent(2, 4, 2, 4),
        Agent(2, 5, 6, 4),
        Agent(2, 6, 4, 3)
    ]

    # Game(board, agents)
    game = Game(board, agents)

    # GAME.set_action(TeamID, AgentID, dx, dy, remove_panel(default: False))
    game.set_action(1, 1, 1, 1)
    game.set_action(1, 2, 0, 1)
    game.set_action(1, 3, 0, 1, remove_panel=True)
    game.set_action(2, 4, 0, 0)
    game.set_action(2, 5, 0, -1, remove_panel=True)
    game.set_action(2, 6, -1, 0)

    # GAME.step()
    game.step()

    # Show board status.
    print(game.board, end="\n\n")
    for agent in game.agents:
        print(agent, end="\n\n")

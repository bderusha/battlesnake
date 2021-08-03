import random
from typing import List, Dict

"""
This file can be a nice home for your move logic, and to write helper functions.

We have started this for you, with a function to help remove the 'neck' direction
from the list of possible moves!
"""


def avoid_body(my_head: Dict[str, int], body: List[dict]):
    """
    my_head: Dictionary of x/y coordinates of the Battlesnake head.
            e.g. {"x": 0, "y": 0}
    my_body: List of dictionaries of x/y coordinates for every segment of a Battlesnake.
            e.g. [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    possible_moves: List of strings. Moves to pick from.
            e.g. ["up", "down", "left", "right"]

    return: The list of remaining possible_moves, with the 'neck' direction removed
    """
    bad_moves = set()
    right = { "x": my_head["x"] + 1, "y": my_head["y"] }
    left = { "x": my_head["x"] - 1, "y": my_head["y"] }
    up = { "x": my_head["x"], "y": my_head["y"] + 1 }
    down = { "x": my_head["x"], "y": my_head["y"] - 1 }
    for part in body:
        print(f"{part} <> {right}")
        if ((part["x"] == right["x"] and part["y"] == right["y"])):
            print("ADD RIGHT")
            bad_moves.add("right")
        print(f"{part} <> {left}")
        if ((part["x"] == left["x"] and part["y"] == left["y"])):
            print("ADD LEFT")
            bad_moves.add("left")
        print(f"{part} <> {up}")
        if ((part["x"] == up["x"] and part["y"] == up["y"])):
            print("ADD UP")
            bad_moves.add("up")
        print(f"{part} <> {down}")
        if ((part["x"] == down["x"] and part["y"] == down["y"])):
            print("ADD DOWN")
            bad_moves.add("down")

    return bad_moves


def avoid_walls(my_head: Dict[str, int], h: int, w: int):
    bad_moves = set()
    if my_head["x"] + 1 >= w:
        bad_moves.add("right")
    if my_head["x"] - 1 < 0:
        bad_moves.add("left")
    if my_head["y"] + 1 >= h:
        bad_moves.add("up")
    if my_head["y"] - 1 < 0:
        bad_moves.add("down")

    return bad_moves


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

    snakes = data["board"]["snakes"]

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    print(f"All board data this turn: {data}")
    print(f"My Battlesnakes head this turn is: {my_head}")
    print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = set({"up", "down", "left", "right"})

    # Don't allow your Battlesnake to move back in on it's own neck
    for snake in snakes:
      possible_moves = possible_moves.difference(avoid_body(my_head, snake["body"]))

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data['board']['height']
    board_width = data['board']['width']

    possible_moves = possible_moves.difference(avoid_walls(my_head, board_height, board_width))
    # TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body


    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    possible_moves = list(possible_moves)
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move

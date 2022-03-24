from dataclasses import dataclass
from faker import Faker
import pydealer
from rich import print
from typing import List

fake = Faker()

@dataclass
class Player:
    hand: pydealer.Stack
    goal_pile: pydealer.Stack
    side_stacks: List[pydealer.Stack]


class SpitePlayer:
    def __init__(self, hand, goal_pile, name, side_stacks):
        self.hand = hand
        self.goal_pile = goal_pile
        self.name = name
        self.side_stacks = side_stacks


@dataclass
class SpiteState:
    players: List[SpitePlayer]
    center_stacks: List[pydealer.Stack]
    draw_pile: pydealer.Stack
    completed_piles: pydealer.Stack
    num_players: int


def setup_game():

    num_of_players = 3
    num_side_stacks = 4
    cards_in_hand = 5
    cards_in_goal = 12

    game_deck = pydealer.Deck() + pydealer.Deck()
    game_deck.shuffle()

    players = []

    for _ in range(num_of_players):
        work_hand = game_deck.deal(cards_in_hand)
        work_goal = game_deck.deal(cards_in_goal)
        work_stacks = [game_deck.deal(1) for _ in range(num_side_stacks)]

        work_player = SpitePlayer(
            hand=work_hand, goal_pile=work_goal, side_stacks=work_stacks, name=fake.first_name(),
        )
        players.append(work_player)

    game_state = SpiteState(
        players=players,
        center_stacks=[],
        draw_pile=game_deck,
        completed_piles=pydealer.Stack(),
        num_players=num_of_players,
    )

    return game_state


def play_game(game_state: SpiteState):

    print(f"Playing a game with {game_state.num_players} players.")

    for player in game_state.players:
        print(f"[bold magenta]{player.name}'s cards:[/bold magenta]")
        print(player.hand)


def main():

    game_state = setup_game()

    play_game(game_state)


if __name__ == "__main__":
    main()

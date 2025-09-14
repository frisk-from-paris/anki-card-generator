""" CLI

Deck name
File path
output name
"""
from datetime import datetime
from argparse import ArgumentParser


def add_arguments(parser: ArgumentParser):
    parser.add_argument(
        "--directory", "-d", type=str, default="data", help="A folder with the cards to create."
    )
    parser.add_argument(
        "--name", "-n", type=str, default=f"deck_{datetime.now()}", help="The name of the deck."
    )
    parser.add_argument(
        "--output", "-o", type=str, default="output", help="The path where to create the deck."
    )

def parse():
    parser = ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()
    return args


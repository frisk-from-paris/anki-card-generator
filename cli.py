""" CLI

Deck name
File path
output name
"""
from datetime import datetime
from argparse import ArgumentParser


def add_arguments(parser: ArgumentParser):
    parser.add_argument(
        "--directory", "-d", type=str, default="", help="A folder with the cards to create."
    )
    parser.add_argument(
        "--name", "-n", type=str, default=f"deck_{datetime.now()}", help="The name of the deck."
    )
    parser.add_argument(
        "--output", "-o", type=str, default="output", help="The path where to create the deck."
    )
    parser.add_argument(
        "--file", "-f", type=str, default="", help="Use a single file."
    )
    parser.add_argument(
        "--translate-to", "-t", type=str, default=None, help="Which way should the translation go (persian or french).",
        required=True
    )


def parse():
    parser = ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()
    return args


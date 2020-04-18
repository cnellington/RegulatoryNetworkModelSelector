"""
Caleb Ellington
CSE 427: Computational Biology
01/25/2020
"""

import argparse
from os.path import isfile
from helpers import *

"""
Usage: align.py <network.txt> <data.txt> [--verbose]
"""
def main():
    parser = argparse.ArgumentParser(description="Protein/DNA alignment")

    parser.add_argument(
        "network",
        action="store",
        help="Location of the network to test",
    )

    parser.add_argument(
        "data",
        action="store",
        help="Location of the experimental data",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="Verbose run",
    )

    args = parser.parse_args()
    if not (isfile(args.network) and isfile(args.data)):
        print("Invalid filepath")
        exit(1)
    reverse_network = parse_network(args.network)
    if args.verbose:
        print(f"reverse network: {reverse_network}")
    data = parse_data(args.data)
    score = score_network(reverse_network, data, verbose=args.verbose)
    print(f"network score: {score}")


if __name__ == '__main__':
    main()

#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit_so_far = prices[1] - prices[0]

    i = 0
    j = 1

    while i < len(prices):

        while j < len(prices):

            if prices[j] - prices[i] > max_profit_so_far:
                max_profit_so_far = prices[j] - prices[i]

            j += 1

        i += 1
        j = i + 1

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

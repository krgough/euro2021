#!/usr/bin/env python3
'''
Created on 1 Jun 2021

@author: keithgough
'''
import json
import logging
import random
import time


LOGGER = logging.getLogger(__name__)

TEAMS_FILE = 'euro2021_teams.json'
PLAYERS_FILE = 'euro2021_players.json'

with open(TEAMS_FILE) as json_file:
    TEAMS = json.load(json_file)['teams']

with open(PLAYERS_FILE) as json_file:
    PLAYERS = json.load(json_file)['players']


def pick_random(my_list):
    """ Pick random selection from a list
        Return the selection and the reduced list
    """
    selection = random.sample(my_list, 1)[0]
    remainder = [item for item in my_list
                 if item['country'] != selection['country']]
    return selection, remainder


def main():
    """ Main Program """

    selections = [{'name': player, 'teams': []}
                  for player in random.sample(PLAYERS, len(PLAYERS))]

    teams = TEAMS

    player = 0
    while len(teams) > 0:
        selection, teams = pick_random(teams)
        selections[player % len(PLAYERS)]['teams'].append(selection)
        player += 1

    print("EURO 2021 - random-selecticator")
    print()
    print("Players: {}".format(PLAYERS))
    print()
    input()
    time.sleep(1)

    name_len = len(max(PLAYERS, key=len)) + 1

    for player in selections:
        p_teams = [team['country'] for team in player['teams']]
        print("{:{}}: {}".format(player['name'], name_len, ", ".join(p_teams)))
        time.sleep(3)

    print('\nAll Done')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()

#!/usr/bin/env python3
'''
Created on 6 Jun 2021

@author: keithgough

Select random teams for Euro 2021 sweepstake

There are 16 games in the playoff round and 24 football teams
We allocate 16 teams to 16 players randomly
At the end of the group stage there is a 16 team playoff to decide
which teams get into the knockout stage.

Any player whose team that did not make it into the 16 team playoff
will get allocated a team randomly from the 8 remaining teams from
the initial selection.

This means all players have a team in the competition up until the
the knockout stages.


'''
import json
import random
import time
import logging

LOGGER = logging.getLogger(__name__)


TEAMS_FILE = 'euro2021_teams.json'
PLAYERS_FILE = 'euro2021_players.json'

with open(TEAMS_FILE) as json_file:
    TEAMS = json.load(json_file)['teams']

with open(PLAYERS_FILE) as json_file:
    PLAYERS = json.load(json_file)['players']


def select_teams():
    """ Select 1 team randomly for each player
    """
    rand_sample = random.sample(TEAMS, len(PLAYERS))
    rand_selection = [team['country'] for team in rand_sample]

    reserve_teams = [team['country'] for team in TEAMS
                     if not team['country'] in rand_selection]


    selections = [{'name': player, 'teams': []}
                  for player in random.sample(PLAYERS, len(PLAYERS))]

    for idx, player in enumerate(selections):
        player['teams'].append(rand_selection[idx])

    return selections, reserve_teams


def print_selections(selections, pause=3):
    """ Print out selections by alphabetical name
    """
    max_name_len = len(max(PLAYERS, key=len)) + 1
    for player_name in sorted(PLAYERS):
        teams = [player['teams'] for player in selections
                 if player['name'] == player_name][0]
        print("{:{}}: {}".format(player_name,
                                 max_name_len,
                                 ', '.join(teams)))
        time.sleep(pause)


def main():
    """ Main Program """

    selections, reserve_teams = select_teams()

    print("EURO 2021 - Random-Selecticator")
    print()
    print("Players: {}".format(", ".join(sorted(PLAYERS))))
    print()
    input("Hit return to make the selections: \n")

    print_selections(selections, pause=2)
    print("\nReserve Teams: {}".format(", ".join(reserve_teams)))
    print('\nAll done.')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()

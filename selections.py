'''
Created on 1 Jun 2021

@author: keithgough
'''

import random
import logging
import time

LOGGER = logging.getLogger(__name__)


TEAMS = [
    {"group": "A", "country": "Italy"},
    {"group": "A", "country": "Switzerland"},
    {"group": "A", "country": "Turkey"},
    {"group": "A", "country": "Wales"},

    {"group": "B", "country": "Belgium"},
    {"group": "B", "country": "Denmark"},
    {"group": "B", "country": "Finland"},
    {"group": "B", "country": "Russia"},

    {"group": "C", "country": "Austria"},
    {"group": "C", "country": "Netherlands"},
    {"group": "C", "country": "North Macedonia"},
    {"group": "C", "country": "Ukraine"},

    {"group": "D", "country": "Croatia"},
    {"group": "D", "country": "Czech Replublic"},
    {"group": "D", "country": "England"},
    {"group": "D", "country": "Scotland"},

    {"group": "E", "country": "Poland"},
    {"group": "E", "country": "Slovakia"},
    {"group": "E", "country": "Spain"},
    {"group": "E", "country": "Sweden"},

    {"group": "F", "country": "France"},
    {"group": "F", "country": "Germany"},
    {"group": "F", "country": "Hungary"},
    {"group": "F", "country": "Portugal"},

    ]


PLAYERS = ['Carmela', 'Keith', 'Luca', 'Nick',
           'Tony Leech', 'Raf', 'James', 'Basia',
           'Tony Moores', 'Ann', 'David', 'Lucia',
           'Paolo'
           ]


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
    #input()
    time.sleep(1)

    name_len = len(max(PLAYERS, key=len)) + 1

    for player in selections:
        p_teams = [team['country'] for team in player['teams']]
        print("{:{}}: {}".format(player['name'], name_len, ", ".join(p_teams)))
        #time.sleep(3)

    print('\nAll Done')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
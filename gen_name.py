import csv
from pprint import pprint
import random

with open(r'names/male_first.txt') as f_male, open(r'names/female_first.txt') as f_female, open(r'names/last.txt') as f_last, open(r'names/nicknames.txt') as f_nickname:
    male = [row[0] for row in csv.reader(f_male)]
    female = [row[0] for row in csv.reader(f_female)]
    first = male + female
    last = [row[0] for row in csv.reader(f_last)]
    nickname = [(position, nickname) for nickname, position in csv.reader(f_nickname)]
    pprint(first)
    pprint(last)
    pprint(nickname)
    for i in range(5):
        current_nickname = random.choice(nickname)
        if int(current_nickname[0]) == 1:
            print('{nick} {first} {last}'.format(nick=current_nickname[1], first=random.choice(first), last=random.choice(last)))
        elif int(current_nickname[0]) == 2:
            print('{first} {last} {nick}'.format(nick=current_nickname[1], first=random.choice(first), last=random.choice(last)))
        else:
            print('{first} {last}'.format(first=random.choice(first), last=random.choice(last)))


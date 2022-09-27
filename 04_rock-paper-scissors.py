#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return f'tie i chose {computer}'
    if is_win(user,computer):
        return f'you won! i chose {computer}'

    return f'you lost! i chose {computer}'

# r > s, s > p, p > r

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True


print(play())

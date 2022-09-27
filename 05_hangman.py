#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from words import words


random_word = words[random.randint(0,len(words))]
a = list(random_word)
guessed = []

print(a)

def guess(x):
    if x in a:
        guessed.append(x)
        print(f'{x} está')
        return




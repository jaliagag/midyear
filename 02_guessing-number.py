#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while True:
        if guess != random_number:
            guess = int(input('give me a number: '))
            if guess > random_number:
                print('demasiado alto')
            elif guess < random_number:
                print('demasiado bajo')
            else:
                print(f'correcto! la respuesta era {random_number}')
                break




guess(10)


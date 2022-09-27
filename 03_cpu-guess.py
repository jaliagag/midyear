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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'so the number must be {guess}')



computer_guess(1000)


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 11:41:33 2017

@author: philmain28
"""
import numpy as np
import matplotlib.pyplot as plt


def lets_play(n, p):
    players = np.linspace(1, n, n)
    player = 0    # start with player 1 (zero index)
    while np.size(players) > 1:    # exit when only one person remains
        sword_throw = np.random.rand()    # roll the dice
        if sword_throw < p:    # if murder attempt is sucessful
            victim = (player + 1) % np.size(players)  # figure out who's next to player
            if victim == 0:
                player -= 1  # correct killer index if player zero gets killed
            players[victim] = 0.
            players = players[players != 0]  # kill them
        player = (player + 1) % np.size(players)
    return players


n_prob = 100
n_games = 1000
people = 39
prob = np.linspace(0.2, 0.9, n_prob)
dist = np.zeros((people, n_prob))
for i in range(1, n_games+1):
    for j in range(0, n_prob):
        [josephus] = lets_play(people, prob[j])
        dist[int(josephus - 1), j] = dist[int(josephus-1), j] + 1


dist = dist / n_games

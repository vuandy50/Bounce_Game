#!/usr/bin/env python3
# Andy Vu
# CPSC 386-04
# 2022-04-19
# avu53@csu.fullerton.edu
# @vuandy50
#
# Lab 12-00
#
# This program runs Bouncing ball Toy
#
"""
Imports the Bounce demo and executes the main function.
"""

import sys
from game import game

if __name__ == "__main__":
    NUM_BALLS = 5
    if len(sys.argv) > 1:
        NUM_BALLS = int(sys.argv[1])
    if NUM_BALLS >= 50:
        NUM_BALLS = 49
    if NUM_BALLS < 3:
        NUM_BALLS = max(NUM_BALLS, 3)
    video_game = game.BounceDemo(NUM_BALLS)
    video_game.build_scene_graph()
    video_game.run()

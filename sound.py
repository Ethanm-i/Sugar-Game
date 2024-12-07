#############################################################
# Module Name: Sugar Pop Sound Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Ethan Mugabe
# Description: The settings implementation of the sugar pop game
#############################################################

import pygame as pg
from settings import *

class Sounds:
    def __init__(self):
        pg.mixer.init()

        self.L = pg.mixer.Sound(sound_dictionary["level"][0])
        self.E = pg.mixer.Sound(sound_dictionary["explode"][0])
        self.C = pg.mixer.Sound(sound_dictionary["sugar_drop"][0])
        self.K = pg.mixer.Sound(sound_dictionary["end"][0])


    def background_music(self):
        self.channelB = pg.mixer.Channel(sound_dictionary["backgrou"][1])
        self.channelB.play(self.B, loops=0)

    def complete_l(self):
        self.channelL = pg.mixer.Channel(sound_dictionary["level"][1])
        self.channelL.play(self.L, loops=0)
    
    def explosion(self):
        self.channelE = pg.mixer.Channel(sound_dictionary["explode"][1])
        self.channelE.play(self.E, loops=0)
    def sugar_d(self):
        self.channelC = pg.mixer.Channel(sound_dictionary["sugar_drop"][1])
        self.channelC.play(self.C, loops=0)
    def end_game(self):
        self.channelK = pg.mixer.Channel(sound_dictionary["end"][1])
        self.channelK.play(self.K, loops=0)
        

    # def play_other_sounds(self, x):
    #     pg.mixer.Sound(sound_dictionary[x]).play()
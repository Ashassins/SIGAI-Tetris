import numpy as np
import random

from keras.models import Sequential, save_model, load_model
from keras.layers import Dense

'''
    output values that we care about:
        score 
        number of lines cleared
        number of pieces placed

        holes in placed pieces
        bumpiness of placed pieces

    reward system
        placed block        small
        cleared line        medium
        tetris completed   big

        game end        negative

        discount: how future rewards are weighted vs immediate ones

    other important params
        loss function
'''

class dNN_model:
    def __init__(self):
        # what parts are important to this model?
        # calls create_model
        self.memory = memory
        self.loss = loss
        self.model = create_model()
        self.learning_rate = learning_rate
        # states

    def create_model():
        # build a DNN model with keras

    def predictScore():
        # predicts the score of the next move
        # Q = S X A
    
    def pickMove():
        # picks what the model will do next/returns best move

    def addMemory():
        # adds move history to the model's memory 

    def sampleMemory():
        # takes a slice of the memory randomly?

    def train(self):
        # this should run the agent ig

    # Simple functions
    def random_score():
        return random.random()

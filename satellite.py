# satellite.py

import numpy as np
from config import SAT_ALTITUDE

class Satellite:

    def __init__(self):

        self.position = np.array([0,0,SAT_ALTITUDE])

    def move(self,t):

        v = 7500

        self.position[0] = v*t

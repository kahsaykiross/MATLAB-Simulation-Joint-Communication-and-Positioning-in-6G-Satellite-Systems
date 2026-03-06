# drone.py

import numpy as np
from config import DRONE_ALTITUDE

class Drone:

    def __init__(self):

        self.position = np.array([0,0,DRONE_ALTITUDE])

    def move(self):

        self.position += np.random.randn(3)

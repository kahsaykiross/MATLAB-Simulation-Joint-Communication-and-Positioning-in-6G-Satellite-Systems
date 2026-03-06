# ris_surface.py

import numpy as np
from config import N_RIS

class RIS:

    def __init__(self):

        self.N = N_RIS
        self.phase = np.zeros(N_RIS)

    def configure(self,phase):

        self.phase = phase

    def reflection_matrix(self):

        return np.diag(np.exp(1j*self.phase))

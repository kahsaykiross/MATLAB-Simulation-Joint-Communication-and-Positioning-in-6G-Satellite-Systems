# localization.py
import numpy as np
from config import C
def estimate_position(ToA,AoA):
 d = C*ToA
 x = d*np.cos(AoA)
    y = d*np.sin(AoA)
 return np.array([x,y])

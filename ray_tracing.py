# ray_tracing.py

import numpy as np
from config import LAMBDA

def pathloss(d):

    return (LAMBDA/(4*np.pi*d))**2

def ray_trace(tx,rx):

    d = np.linalg.norm(tx-rx)

    pl = pathloss(d)

    phase = np.exp(-1j*2*np.pi*d/LAMBDA)

    return pl*phase

# channel_model.py
import numpy as np
from config import N_TX,N_RX
def mimo_channel():
 H = (np.random.randn(N_RX,N_TX)+1j*np.random.randn(N_RX,N_TX))/np.sqrt(2)
 return H

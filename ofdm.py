# ofdm.py
import numpy as np
def ofdm_modulate(symbols):
return np.fft.ifft(symbols)
def ofdm_demodulate(signal):
return np.fft.fft(signal)

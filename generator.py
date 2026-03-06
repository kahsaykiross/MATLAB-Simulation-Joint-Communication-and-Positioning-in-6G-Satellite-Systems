# generator.py

import numpy as np

def generate_dataset(N=200000):

    data = []

    for i in range(N):

        channel = np.random.randn(128)

        phase = np.random.uniform(0,2*np.pi,128)

        snr = np.random.uniform(0,30)

        gain = np.abs(np.sum(channel*np.exp(1j*phase)))

        capacity = np.log2(1+gain**2)

        position_error = np.random.rand()*5

        data.append([snr,capacity,position_error])

    return np.array(data)

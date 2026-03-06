import pandas as pd

def generate_dataset(samples=50000,Nris=64):

    data = []

    for i in range(samples):

        channel = np.random.randn(Nris)

        phase = np.random.uniform(0,2*np.pi,Nris)

        gain = np.abs(np.sum(channel*np.exp(1j*phase)))

        capacity = np.log2(1+gain**2)

        position_error = np.random.rand()*5

        snr = np.random.uniform(0,30)

        reward = capacity - 0.1*position_error

        sample = np.concatenate([channel,phase,[snr,capacity,position_error,reward]])

        data.append(sample)

    data = np.array(data)

    return data

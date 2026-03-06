# multiuser_ris_optimizer.py

import numpy as np

def optimize_ris(H_br,H_ru):

    N = H_br.shape[0]

    phase = np.zeros(N)

    for i in range(N):

        phase[i] = np.angle(np.sum(H_ru[:,i]*H_br[i,:]))

    return phase

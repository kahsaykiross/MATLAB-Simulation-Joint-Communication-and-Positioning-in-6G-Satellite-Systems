# main.py

import numpy as np
from environment.satellite import Satellite
from environment.drone import Drone
from environment.ris_surface import RIS
from channel.ray_tracing import ray_trace
from optimization.multiuser_ris_optimizer import optimize_ris

sat = Satellite()
drone = Drone()
ris = RIS()

for t in range(100):

    sat.move(t)
    drone.move()

    H_br = np.random.randn(128,16)
    H_ru = np.random.randn(4,128)

    phase = optimize_ris(H_br,H_ru)

    ris.configure(phase)

    print("Time:",t,"RIS configured")

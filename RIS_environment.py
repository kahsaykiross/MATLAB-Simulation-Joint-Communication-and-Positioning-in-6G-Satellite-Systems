import torch
import numpy as np

class RISEnvironment:

    def __init__(self,Nris=64):

        self.Nris = Nris
        self.state_dim = 128
        self.action_dim = Nris

        self.reset()

    def reset(self):

        self.channel = torch.randn(self.state_dim)

        return self.channel

    def step(self,action):

        phase = torch.exp(1j*action)

        gain = torch.abs(torch.sum(self.channel[:self.Nris]*phase))

        capacity = torch.log2(1+gain**2)

        position_error = torch.abs(torch.sum(self.channel[self.Nris:2*self.Nris]))

        reward = capacity - 0.1*position_error

        next_state = torch.randn(self.state_dim)

        done = False

        return next_state,reward,done

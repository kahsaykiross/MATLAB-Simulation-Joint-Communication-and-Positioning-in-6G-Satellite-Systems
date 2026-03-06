import torch.nn as nn

class Actor(nn.Module):

    def __init__(self,state_dim,action_dim):

        super().__init__()

        self.net = nn.Sequential(

            nn.Linear(state_dim,256),
            nn.ReLU(),

            nn.Linear(256,256),
            nn.ReLU(),

            nn.Linear(256,action_dim),
            nn.Tanh()

        )

    def forward(self,state):

        return np.pi*self.net(state)

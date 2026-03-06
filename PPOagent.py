class PPOPolicy(nn.Module):

    def __init__(self,state_dim,action_dim):

        super().__init__()

        self.fc = nn.Sequential(

            nn.Linear(state_dim,256),
            nn.ReLU(),

            nn.Linear(256,256),
            nn.ReLU(),

            nn.Linear(256,action_dim)

        )

    def forward(self,state):

        return np.pi*torch.tanh(self.fc(state))

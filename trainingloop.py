env = RISEnvironment()

state_dim = env.state_dim
action_dim = env.action_dim

actor = Actor(state_dim,action_dim)

optimizer = torch.optim.Adam(actor.parameters(),lr=1e-4)

episodes = 2000

for ep in range(episodes):

    state = torch.tensor(env.reset(),dtype=torch.float32)

    total_reward = 0

    for step in range(200):

        action = actor(state)

        next_state,reward,done = env.step(action.detach())

        loss = -reward

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        state = torch.tensor(next_state,dtype=torch.float32)

        total_reward += reward

    if ep%100==0:

        print("Episode:",ep,"Reward:",total_reward)

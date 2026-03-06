# federated_learning.py
import torch
def federated_average(models):
global_model = models[0]
for param in global_model.parameters():
 param.data = torch.mean(
            torch.stack([m.state_dict()[param.name] for m in models]),
            dim=0
)
return global_model

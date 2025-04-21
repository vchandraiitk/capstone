import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(4, 1)

    def forward(self, x):
        return self.linear(x)

def save_model(path="model.pt"):
    model = SimpleModel()
    torch.save(model, path)
    print("✅ model.pt saved")

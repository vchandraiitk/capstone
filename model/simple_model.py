# model.py
import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(4, 1)

    def forward(self, x):
        return self.linear(x)

def save_model():
    model = SimpleModel()
    torch.save(model, "model.pt")
    print("✅ model.pt created")

if __name__ == "__main__":
    save_model()

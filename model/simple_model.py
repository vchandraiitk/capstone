import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self, input_size=4, output_size=1):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(input_size, output_size)

    def forward(self, x):
        return self.linear(x)

# Save the model weights
if __name__ == "__main__":
    model = SimpleModel()
    torch.save(model.state_dict(), "artifacts/simple_model.pt")
    print("✅ Model saved to artifacts/simple_model.pt")


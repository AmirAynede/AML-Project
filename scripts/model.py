import torch.nn as nn
from torchvision import models
from torchvision.models import ResNet18_Weights

def build_model(num_classes):
    # Load ResNet18 with the recommended weights
    weights = ResNet18_Weights.DEFAULT
    model = models.resnet18(weights=weights)

    # Freeze early layers (optional)
    for param in model.parameters():
        param.requires_grad = False

    # Replace the final classification layer to match num_classes
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)

    return model

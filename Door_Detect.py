import torch
import torch.nn as nn
import torchvision
from torchvision import models, transforms
from torchvision.models import ResNet18_Weights
from PIL import Image
# Loads model stored within the file system
def load():
    checkpoint = torch.load('model.pth')
    model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
    nr_filters = model.fc.in_features
    model.fc = nn.Linear(nr_filters, 1)
    model.load_state_dict(checkpoint)
    return model

# Inputs a single image into the model and returns the predicted image state
def detect(model, path):
    model.eval()
    image = Image.open(path)
    data_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406],
        std=[0.229,0.224,0.225])
    ])
    image = data_transforms(image).float()
    image = image.detach().clone()
    image = image.unsqueeze(0)
    decision = torch.sigmoid(model(image))
    print(decision)
    # Converts numerical evaluation to its representative state
    return "Closed" if decision < 0.5 else "Open"
    

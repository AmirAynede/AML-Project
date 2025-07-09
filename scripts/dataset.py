import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def prepare_dataloaders(train_path, val_path, test_path=None, batch_size=32, num_workers=2):
    # Common image transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    train_set = datasets.ImageFolder(train_path, transform=transform)
    val_set = datasets.ImageFolder(val_path, transform=transform)
    test_set = datasets.ImageFolder(test_path, transform=transform) if test_path else None

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_set, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=num_workers) if test_set else None
    
    class_names = train_set.classes

    return train_loader, val_loader, test_loader, class_names

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler # TODO
import torch.backends.cudnn as cudnn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
from PIL import Image
from tempfile import TemporaryDirectory # TODO

cudnn.benchmark = True # TODO
plt.ion() # interactive mode

device = (
    'cuda' if torch.cuda.is_available() 
    else "mps" if torch.backends.mps.is_available()
    else 'cpu'
)

data_transforms = {
    'train': transforms.Compose([

    ]),
    'val': transforms.Compose([

    ]),
}

def get_device():
    print(f"Using {device} device")
    return device

if __name__ == "__main__":
    get_device()
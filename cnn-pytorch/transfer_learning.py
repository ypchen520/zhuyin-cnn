import torch

device = (
    'cuda' if torch.cuda.is_available() 
    else "mps" if torch.backends.mps.is_available()
    else 'cpu'
)

def get_device():
    print(f"Using {device} device")
    return device

if __name__ == "__main__":
    get_device()
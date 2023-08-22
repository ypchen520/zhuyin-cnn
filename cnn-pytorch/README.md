# Transfer Learning for Computer Vision

[PyTorch tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

## Two Major Transfer Learning Scenarios

- Finetuning the ConvNet
  - Initialize the network with a pretrained network
  - Rest of the training looks as usual
- ConvNet as fixed feature extractor
  - Freeze the weights for all of the network except weights of the final fully connected layer
  - The last layer is replaced with a new layer (fully connected) with random weights and only this layer is trained

### Load Data

- The tutorial uses 120 training images each for ants and bees. 
  - There are 75 validation images for each class.
- [`datasets.ImageFolder`](https://pytorch.org/vision/stable/generated/torchvision.datasets.ImageFolder.html)

```
data/
└── hymenoptera_data
    ├── train
    │   ├── ants
    │   └── bees
    └── val
        ├── ants
        └── bees
```

#### Zhuyin Dataset

- 16 classes
  - b, p, m, f, d, l, t, s, g, ch, en, eng, o, e, ts, k
  - 10 repetitions for 6 participants
  - 60 for each gesture
    - 54 for training, 6 for validation
- File structure modification:

  ```
  data/
  └── zmg
      ├── train
      │   ├── b
      |   ├── ...
      │   └── k
      └── val
          ├── b
          ├── ...
          └── k
  ```



## Open-Source Models for Computer Vision (Note)

- HuggingFace
- Model Zoo
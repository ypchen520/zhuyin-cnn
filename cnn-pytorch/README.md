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

#### Zhuyin Dataset

- 16 classes
  - b, p, m, f, d, l, t, s, g, ch, en, eng, o, e, ts, k

## Open-Source Models for Computer Vision (Note)

- HuggingFace
- Model Zoo
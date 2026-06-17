import torch
from torch import nn
from torchsummary import summary



class Residual(nn.Module):
    def __init__(self):
        super().__init__()